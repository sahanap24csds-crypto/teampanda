import pandas as pd
import time
from datetime import datetime
from sklearn.ensemble import IsolationForest
from sklearn.linear_model import LinearRegression
import numpy as np

FILE_PATH = "sample.csv"

# =============================
# ₹ FORMAT
# =============================
def format_rupee(x):
    return f"₹{x:,.0f}"


# =============================
# LOAD + FEATURES
# =============================
def load_and_process():
    df = pd.read_csv(FILE_PATH)

    df.rename(columns={"Payment Mode": "Payment_Mode"}, inplace=True)

    df['DateTime'] = pd.to_datetime(df['Date'] + ' ' + df['Time'])
    df['hour'] = df['DateTime'].dt.hour
    df['day'] = df['DateTime'].dt.day
    df['weekday'] = df['DateTime'].dt.weekday
    df['is_weekend'] = df['weekday'].isin([5, 6]).astype(int)

    return df


# =============================
# ANOMALY DETECTION
# =============================
def add_anomaly(df):
    model = IsolationForest(contamination=0.15, random_state=42)
    df['anomaly'] = model.fit_predict(df[['Amount', 'hour', 'is_weekend']])
    return df


# =============================
# PATTERN DETECTIONS
# =============================
def late_night(df): return df[df['hour'] < 5]
def micro(df): return df[df['Amount'] < 50]
def impulse(df): return df[(df['hour'] >= 20) & (df['Amount'] > 200)]
def subscriptions(df): return df[df['Subscription'] == 'Yes']


# =============================
# 📉 PREDICTION ENGINE
# =============================
def forecast_spending(df):

    df['date_only'] = df['DateTime'].dt.date
    daily = df.groupby('date_only')['Amount'].sum().reset_index()

    # Convert dates → numbers
    daily['t'] = np.arange(len(daily))

    model = LinearRegression()
    model.fit(daily[['t']], daily['Amount'])

    # Predict next 3 days
    future_t = np.array(range(len(daily), len(daily) + 3)).reshape(-1, 1)
    preds = model.predict(future_t)

    return preds


def predict_loss_risk(df):

    recent = df.tail(5)['Amount'].mean()
    overall = df['Amount'].mean()

    if recent > overall * 1.5:
        return "HIGH"
    elif recent > overall:
        return "MODERATE"
    else:
        return "LOW"


# =============================
# 🎯 DECISION ENGINE
# =============================
def decision_agent(df, predictions, risk_level):

    actions = []

    if len(late_night(df)) > 2:
        actions.append("Set spending limit after 10 PM")

    if len(micro(df)) > 5:
        actions.append("Enable daily expense tracking")

    if len(subscriptions(df)) > 2:
        actions.append("Cancel unused subscriptions immediately")

    if len(impulse(df)) > 1:
        actions.append("Add 24-hour delay before big purchases")

    if risk_level == "HIGH":
        actions.append("⚠️ Freeze non-essential spending for next 3 days")

    if np.mean(predictions) > df['Amount'].mean():
        actions.append("⚠️ Future spending increasing — apply strict budget")

    return actions


# =============================
# MAIN LOOP
# =============================
def run_agent():

    print("\n🤖 AUTONOMOUS PREDICTION + DECISION AGENT STARTED\n")

    last_rows = 0

    while True:
        try:
            df = load_and_process()
            df = add_anomaly(df)

            if len(df) > last_rows:

                print("\n" + "="*60)
                print("📊 AI FINANCIAL PREDICTION & DECISION REPORT")
                print("="*60)

                # 📉 Forecast
                predictions = forecast_spending(df)

                print("\n📉 FUTURE SPENDING FORECAST (Next 3 Days):")
                for i, val in enumerate(predictions, 1):
                    print(f"   Day {i}: {format_rupee(val)}")

                # ⚠️ Risk Prediction
                risk_level = predict_loss_risk(df)

                print("\n⚠️ LOSS RISK PREDICTION:")
                print(f"   → {risk_level} RISK")

                # 🎯 Decision Actions
                actions = decision_agent(df, predictions, risk_level)

                print("\n🎯 RECOMMENDED ACTIONS:")
                if actions:
                    for act in actions:
                        print(f"   - {act}")
                else:
                    print("   No immediate actions required")

                # 🚨 Anomalies
                anomalies = df[df['anomaly'] == -1]
                if len(anomalies) > 0:
                    print("\n🚨 UNUSUAL TRANSACTIONS:")
                    for _, row in anomalies.iterrows():
                        print(f"   - {row['Date']} {row['Time']} | {row['Category']} | {format_rupee(row['Amount'])}")

                last_rows = len(df)

            else:
                print("No new transactions...")

        except Exception as e:
            print("Error:", e)

        time.sleep(10)


if __name__ == "__main__":
    run_agent()