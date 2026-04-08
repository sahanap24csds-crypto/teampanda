import pandas as pd
import time
from datetime import datetime
from sklearn.ensemble import IsolationForest

FILE_PATH = "sample.csv"



def format_rupee(x):
    return f"₹{x:,.0f}"




def load_and_process():
    df = pd.read_csv(FILE_PATH)

    df.rename(columns={"Payment Mode": "Payment_Mode"}, inplace=True)

    df['DateTime'] = pd.to_datetime(df['Date'] + ' ' + df['Time'])

    df['hour'] = df['DateTime'].dt.hour
    df['day'] = df['DateTime'].dt.day
    df['weekday'] = df['DateTime'].dt.weekday
    df['is_weekend'] = df['weekday'].isin([5, 6]).astype(int)

    return df




def add_anomaly_column(df):
    features = df[['Amount', 'hour', 'is_weekend']]

    model = IsolationForest(contamination=0.15, random_state=42)
    df['anomaly'] = model.fit_predict(features)

    return df




def late_night(df):
    return df[df['hour'] < 5]

def micro_leak(df):
    return df[df['Amount'] < 50]

def velocity(df):
    df = df.sort_values(by='DateTime')
    df['diff'] = df['DateTime'].diff().dt.total_seconds()
    return df[df['diff'] < 120]

def impulse(df):
    return df[(df['hour'] >= 20) & (df['Amount'] > 200)]

def subscriptions(df):
    return df[df['Subscription'] == 'Yes']

def payday_surge(df):
    early = df[df['day'] <= 5]['Amount'].sum()
    rest = df[df['day'] > 5]['Amount'].sum()
    return early > rest




def print_summary(df):

    print("\n" + "="*50)
    print("🔍 PERSONAL FINANCIAL ANALYSIS REPORT")
    print("="*50)

    print(f"\n🌙 Late Night Transactions: {len(late_night(df))}")

    weekend = df[df['is_weekend'] == 1]['Amount'].sum()
    weekday = df[df['is_weekend'] == 0]['Amount'].sum()

    print(f"📅 Weekend Spend: {format_rupee(weekend)}")
    print(f"📅 Weekday Spend: {format_rupee(weekday)}")

    print(f"\n💸 Micro Transactions (<₹50): {len(micro_leak(df))}")

    
    subs = subscriptions(df)
    print("\n📺 Active Subscriptions:")
    if len(subs) > 0:
        for _, row in subs.iterrows():
            print(f"   - {row['Category']} : {format_rupee(row['Amount'])}")
    else:
        print("   None")

    print(f"\n💰 Payday Surge: {'Yes' if payday_surge(df) else 'No'}")
    print(f"⚡ High Velocity Transactions: {len(velocity(df))}")
    print(f"🛒 Impulse Purchases: {len(impulse(df))}")

    
    print("\n💳 Payment Behavior (Average Spend):")
    payment = df.groupby('Payment_Mode')['Amount'].mean()
    for mode, amt in payment.items():
        print(f"   - {mode}: {format_rupee(amt)}")




def risk_breakdown(df):

    breakdown = {}

    breakdown['late_night'] = len(late_night(df)) // 2
    breakdown['micro_leak'] = len(micro_leak(df)) // 5
    breakdown['velocity'] = len(velocity(df)) // 2
    breakdown['impulse'] = len(impulse(df))
    breakdown['payday'] = 1 if payday_surge(df) else 0
    breakdown['subscriptions'] = 1 if len(subscriptions(df)) > 2 else 0
    breakdown['anomalies'] = len(df[df['anomaly'] == -1])

    return breakdown


def total_risk_score(breakdown):
    return sum(breakdown.values())




def generate_recommendations(df):

    recs = []

    if len(late_night(df)) > 2:
        recs.append("Reduce late-night spending")

    if len(micro_leak(df)) > 5:
        recs.append("Track small expenses")

    if len(subscriptions(df)) > 2:
        recs.append("Cancel unused subscriptions")

    if len(impulse(df)) > 1:
        recs.append("Avoid high-value purchases at night")

    return recs



def spending_trend(df):
    df['date_only'] = df['DateTime'].dt.date
    return df.groupby('date_only')['Amount'].sum().tail(5)


def user_profile(df):

    if len(late_night(df)) > 3:
        return "Night Spender"
    elif len(micro_leak(df)) > 8:
        return "Micro-Spender"
    else:
        return "Balanced User"



def run_agent():

    print("\n🤖 FINAL SMART FINANCIAL AGENT STARTED\n")

    last_rows = 0

    while True:
        try:
            df = load_and_process()
            df = add_anomaly_column(df)

            if len(df) > last_rows:

                print(f"\n🕒 {datetime.now().strftime('%H:%M:%S')}")

                print_summary(df)

                breakdown = risk_breakdown(df)
                score = total_risk_score(breakdown)

                print("\n" + "="*50)
                print("📊 RISK ANALYSIS")
                print("="*50)

                print(f"\n🔢 Overall Risk Score: {score}")

                if score >= 8:
                    print("🚨 Status: HIGH RISK USER")
                elif score >= 4:
                    print("⚠️ Status: MODERATE RISK USER")
                else:
                    print("✅ Status: LOW RISK USER")

                print("\n📉 Risk Breakdown:")
                for k, v in breakdown.items():
                    print(f"   - {k.replace('_',' ').title()}: +{v}")

                print("\n💡 SMART RECOMMENDATIONS:")
                recs = generate_recommendations(df)
                if recs:
                    for r in recs:
                        print(f"   - {r}")
                else:
                    print("   No major recommendations")

                print("\n📈 Recent Spending Trend:")
                trend = spending_trend(df)
                for date, amt in trend.items():
                    print(f"   - {date}: {format_rupee(amt)}")

                print("\n👤 User Profile:")
                print(f"   → {user_profile(df)}")

                anomalies = df[df['anomaly'] == -1]
                if len(anomalies) > 0:
                    print("\n🚨 Anomalous Transactions:")
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