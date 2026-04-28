import pandas as pd
from sklearn.ensemble import IsolationForest

def detect_anomalies():
    df = pd.read_csv("data/sample_data.csv")

    model = IsolationForest(contamination=0.02, random_state=42)
    df["anomaly"] = model.fit_predict(df[["amount"]])

    anomalies = df[df["anomaly"] == -1]
    anomalies.to_csv("data/anomalies.csv", index=False)

    print(f"Detected {len(anomalies)} anomalies")

if __name__ == "__main__":
    detect_anomalies()
