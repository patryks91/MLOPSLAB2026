from pathlib import Path
from typing import Literal, cast

import joblib
from sentence_transformers import SentenceTransformer
from sklearn.linear_model import LogisticRegressionCV


Sentiment = Literal["negative", "neutral", "positive"]

MODELS_DIR = Path(__file__).resolve().parent / "models"

LABELS: dict[int, Sentiment] = {
    0: "negative",
    1: "neutral",
    2: "positive",
}


class SentimentModel:
    def __init__(self) -> None:
        self.encoder = SentenceTransformer(
            str(MODELS_DIR / "sentence_transformer.model"),
            device="cpu",
            local_files_only=True,
        )
        self.classifier = cast(
            LogisticRegressionCV,
            joblib.load(MODELS_DIR / "classifier.joblib"),
        )

    def predict(self, text: str) -> Sentiment:
        embeddings = self.encoder.encode([text])
        predicted_class = int(self.classifier.predict(embeddings)[0])

        return LABELS[predicted_class]
