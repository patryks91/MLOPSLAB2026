from pathlib import Path

import joblib


MODEL_PATH = Path(__file__).resolve().parent / "model.joblib"


def load_model():
    return joblib.load(MODEL_PATH)


def predict(artifact, features: list[float]) -> str:
    model = artifact["model"]
    target_names = artifact["target_names"]

    predicted_class = model.predict([features])[0]

    return str(target_names[predicted_class])
