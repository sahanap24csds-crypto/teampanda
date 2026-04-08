import pandas as pd
from sklearn.ensemble import IsolationForest

FOOD_LIMIT = 2000
MAX_TXN_PER_DAY = 5
SAVINGS_GOAL = 5000
MONTHLY_INCOME = 15000


def load_data(file):
    df = pd.read_csv(file)
    df['date'] = pd.to_datetime(df['date'])
    return df

def rule_based_detection(df):
    print("📌 Rule-Based Checks:")

    food_spending = df[df['category'] == 'Food']['amount'].sum()
    if food_spending > FOOD_LIMIT:
        print(f"⚠️ Food Leak: ₹{food_spending}")

    txn_per_day = df.groupby(df['date'].dt.date).size()
    for day, count in txn_per_day.items():
        if count > MAX_TXN_PER_DAY:
            print(f"⚠️ Too many transactions on {day}: {count}")

    total_spent = df['amount'].sum()
    if total_spent > (MONTHLY_INCOME - SAVINGS_GOAL):
        print("⚠️ Savings goal at risk!")

def ml_detection(df):
    print("\n🤖 ML-Based Detection:")

    model = IsolationForest(contamination=0.2, random_state=42)
    df['anomaly'] = model.fit_predict(df[['amount']])

    anomalies = df[df['anomaly'] == -1]

    if len(anomalies) == 0:
        print("✅ No unusual behavior detected")
    else:
        for _, row in anomalies.iterrows():
            print(f"⚠️ ML Leak: ₹{row['amount']} in {row['category']}")

def predict_future_spending(df):
    days = df['date'].dt.day.nunique()
    if days == 0:
        return

    total_spent = df['amount'].sum()
    avg_per_day = total_spent / days
    predicted_month = avg_per_day * 30

    print("\n🔮 Future Prediction:")
    print(f"Estimated monthly spending: ₹{int(predicted_month)}")

    if predicted_month > (MONTHLY_INCOME - SAVINGS_GOAL):
        print("⚠️ You may NOT reach your savings goal at this rate!")


def top_leak_source(df):
    category_total = df.groupby('category')['amount'].sum()
    top_category = category_total.idxmax()

    print("\n💸 Biggest Expense Category:", top_category)

def time_pattern(df):
    df['hour'] = df['date'].dt.hour

    late_spending = df[df['hour'] > 22]

    if len(late_spending) > 0:
        print("\n🌙 Late-night spending detected → possible impulse behavior")

def generate_summary(df):
    total_spent = df['amount'].sum()
    print("\n📊 SUMMARY")
    print(f"Total Spending: ₹{total_spent}")

def run_system(file):
    df = load_data(file)

    print("🔍 Hybrid Leak Detection System\n")

    rule_based_detection(df)
    ml_detection(df)
    predict_future_spending(df)

    top_leak_source(df)
    time_pattern(df)

    generate_summary(df)


if __name__ == "__main__":
    run_system("expenses.csv")