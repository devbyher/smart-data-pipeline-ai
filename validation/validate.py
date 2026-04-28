import pandas as pd

def validate_data():
    df = pd.read_csv("data/sample_data.csv")

    assert df["transaction_id"].is_unique, "Duplicate IDs found!"
    assert df["amount"].notnull().all(), "Null values found!"

    print("Validation Passed Successfully")

if __name__ == "__main__":
    validate_data()
