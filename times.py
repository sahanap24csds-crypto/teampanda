import pandas as pd
from io import StringIO

# -----------------------------
# 1. LOAD DATA
# -----------------------------
data = """Date Time,Amount,Category,Payment Mode,User Income,Subscription
2023-01-01 01:00:00,1575,Travel,Card,30000,No
2023-01-01 02:00:00,1768,Groceries,UPI,100000,No
2023-01-01 06:00:00,2540,Travel,Card,100000,No
2023-01-02 01:00:00,960,Food,Card,30000,No
2023-01-02 14:00:00,3510,Food,Net Banking,50000,Yes
2023-01-03 04:00:00,119,Food,Cash,100000,Yes
2023-01-03 18:00:00,2666,Travel,Card,50000,No
"""

df = pd.read_csv(StringIO(data))

# -----------------------------
# 2. FEATURE ENGINEERING
# -----------------------------
df["Date Time"] = pd.to_datetime(df["Date Time"])

# Time patterns
df["Hour"] = df["Date Time"].dt.hour
df["Day"] = df["Date Time"].dt.day_name()
df["Date"] = df["Date Time"].dt.date

# -----------------------------
# 3. SPENDING FREQUENCY
# -----------------------------
daily_summary = (
    df.groupby("Date")
    .agg(
        Transactions=("Amount", "count"),
        Total_Spend=("Amount", "sum"),
        Avg_Spend=("Amount", "mean"),
    )
    .reset_index()
)

category_summary = (
    df.groupby("Category")
    .agg(Total_Spend=("Amount", "sum"), Frequency=("Amount", "count"))
    .reset_index()
)

# -----------------------------
# 4. AUTOMATIC INSIGHTS
# -----------------------------
peak_hour = df.groupby("Hour")["Amount"].sum().idxmax()
top_category = df.groupby("Category")["Amount"].sum().idxmax()
top_day = df["Day"].mode()[0]

# -----------------------------
# 5. OUTPUT
# -----------------------------
print("\nTIME PATTERNS:\n")
print(df[["Date Time", "Hour", "Day"]])

print("\nDAILY SPENDING SUMMARY:\n")
print(daily_summary)

print("\nCATEGORY SUMMARY:\n")
print(category_summary)

print("\nAUTO DETECTED INSIGHTS:\n")
print(f"Peak spending hour: {peak_hour}")
print(f"Most active category: {top_category}")
print(f"Most frequent day: {top_day}")
