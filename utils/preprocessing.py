import pandas as pd

# Load dataset
def load_data(file_path):
    try:
        df = pd.read_csv(file_path)
        print("Data loaded successfully")
        return df
    except Exception as e:
        print("Error loading data:", e)
        return None


# Inspect dataset
def inspect_data(df):
    print("\nFirst 5 rows:")
    print(df.head())

    print("\nInfo:")
    print(df.info())

    print("\nMissing values:")
    print(df.isnull().sum())


# Clean missing values
def clean_missing_values(df):
    df = df.dropna()
    print("Missing values removed")
    return df


# Convert data types
def convert_types(df):
    for col in df.columns:
        try:
            df[col] = pd.to_numeric(df[col])
        except:
            pass
    print("Data types converted where possible")
    return df


# Remove invalid values
def remove_invalid(df):
    df = df[df.select_dtypes(include=['number']).ge(0).all(axis=1)]
    print("Invalid values removed")
    return df