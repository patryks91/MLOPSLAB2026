import pytest
from pydantic import ValidationError

from api.models.sentiment import PredictRequest, PredictResponse


def test_valid_text() -> None:
    request = PredictRequest(text="  Great lecture!  ")

    assert request.text == "Great lecture!"


@pytest.mark.parametrize("text", ["", "   ", "\n\t"])
def test_empty_text_rejected(text: str) -> None:
    with pytest.raises(ValidationError):
        PredictRequest(text=text)


def test_invalid_text_type_rejected() -> None:
    with pytest.raises(ValidationError):
        PredictRequest.model_validate({"text": 123})


@pytest.mark.parametrize("prediction", ["negative", "neutral", "positive"])
def test_valid_prediction(prediction: str) -> None:
    response = PredictResponse.model_validate({"prediction": prediction})

    assert response.prediction == prediction


def test_invalid_prediction_rejected() -> None:
    with pytest.raises(ValidationError):
        PredictResponse.model_validate({"prediction": "unknown"})
