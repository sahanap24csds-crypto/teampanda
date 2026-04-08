import pandas as pd

# Load dataset
data = pd.read_csv("synthetic_finance_data.csv")

# Convert Date Time
data["Date Time"] = pd.to_datetime(data["Date Time"])

# Remove duplicates
data = data.drop_duplicates()

# Remove missing values
data = data.dropna()

# Remove invalid amounts
data = data[data["Amount"] > 0]

# Sort data
data = data.sort_values("Date Time")

# Reset index
data = data.reset_index(drop=True)

# Convert datatypes

# 1. Date Time → datetime
data["Date Time"] = pd.to_datetime(data["Date Time"])

# 2. Amount → integer
data["Amount"] = data["Amount"].astype(int)

# 3. Category → category
data["Category"] = data["Category"].astype("category")

# 4. Payment Mode → category
data["Payment Mode"] = data["Payment Mode"].astype("category")

# 5. User Income → integer
data["User Income"] = data["User Income"].astype(int)

# 6. Subscription → category
data["Subscription"] = data["Subscription"].astype("category")
# Save cleaned file
data.to_csv("cleaned_finance_data.csv", index=False)

print("Cleaned file created!")