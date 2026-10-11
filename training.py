from pathlib import Path

import joblib
from sklearn.datasets import load_iris
from sklearn.ensemble import RandomForestClassifier


MODEL_PATH = Path(__file__).resolve().parent / "model.joblib"


def load_data():
    return load_iris()


def train_model(data):
    model = RandomForestClassifier(random_state=42)
    model.fit(data.data, data.target)
    return model


def save_model(model, target_names):
    artifact = {
        "model": model,
        "target_names": target_names,
    }
    joblib.dump(artifact, MODEL_PATH)


if __name__ == "__main__":
    data = load_data()
    model = train_model(data)
    save_model(model, data.target_names)

    print(f"Model zapisany w: {MODEL_PATH}")
