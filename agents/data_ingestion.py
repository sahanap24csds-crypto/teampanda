from utils.preprocessing import load_data, inspect_data, clean_missing_values, convert_types, remove_invalid

def data_ingestion_agent(file_path):
    df = load_data(file_path)

    if df is not None:
        inspect_data(df)
        df = clean_missing_values(df)
        df = convert_types(df)
        df = remove_invalid(df)

        print("Data Cleaning Completed")

    return df