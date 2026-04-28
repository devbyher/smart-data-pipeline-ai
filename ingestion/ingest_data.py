import pandas as pd
import numpy as np
import os

os.makedirs("data", exist_ok=True)

def generate_data():
    np.random.seed(42)

    data = pd.DataFrame({
        "transaction_id": range(1, 1001),
        "amount": np.random.normal(5000, 2000, 1000),
        "timestamp": pd.date_range(start="2024-01-01", periods=1000, freq="H")
    })

    # Inject anomalies
    data.loc[::50, "amount"] = data["amount"] * 5

    data.to_csv("data/sample_data.csv", index=False)
    print("Data generated successfully")

if __name__ == "__main__":
    generate_data()
