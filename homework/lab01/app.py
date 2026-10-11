from fastapi import FastAPI

from api.models.sentiment import PredictRequest, PredictResponse
from inference import SentimentModel


app = FastAPI(title="Sentiment Analysis API")
model = SentimentModel()


@app.post("/predict")
def predict(request: PredictRequest) -> PredictResponse:
    prediction = model.predict(request.text)

    return PredictResponse(prediction=prediction)
