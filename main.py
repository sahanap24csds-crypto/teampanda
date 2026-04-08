import sys
import os
sys.path.append(os.path.dirname(os.path.abspath(__file__))) 
from agents.data_ingestion import data_ingestion_agent

def main():
    file_path =  r"C:\Users\jssru\OneDrive\hackthon\cleaned_finance_data.csv"
    df = data_ingestion_agent(file_path)

if __name__ == "__main__":
    main()