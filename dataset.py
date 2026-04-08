import pandas as pd
import numpy as np

np.random.seed(42)

n = 10000

dates = pd.date_range(start="2023-01-01", periods=n, freq="h")

categories = ["Food", "Shopping", "Travel", "Entertainment", "Groceries", "Transport"]
payment_modes = ["UPI", "Card", "Cash", "Net Banking"]

data = pd.DataFrame({
    "Date Time": np.random.choice(dates, n),
    "Amount": np.random.randint(50, 5000, n),
    "Category": np.random.choice(categories, n),
    "Payment Mode": np.random.choice(payment_modes, n),
    "User Income": np.random.choice([30000, 50000, 70000, 100000], n),
    "Subscription": np.random.choice(["Yes", "No"], n, p=[0.2, 0.8])
})

data.to_csv("synthetic_finance_data.csv", index=False)