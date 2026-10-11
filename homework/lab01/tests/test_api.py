import pytest
from fastapi.testclient import TestClient

from app import app


client = TestClient(app)


def test_predict_response() -> None:
    response = client.post(
        "/predict",
        json={"text": "What a great MLOps lecture!"},
    )

    assert response.status_code == 200
    assert response.headers["content-type"].startswith("application/json")

    body = response.json()

    assert set(body) == {"prediction"}
    assert body["prediction"] in {"negative", "neutral", "positive"}


@pytest.mark.parametrize(
    "payload",
    [
        {},
        {"text": ""},
        {"text": "   "},
        {"text": 123},
        {"text": None},
        {"text": "Hello", "extra": "unexpected"},
    ],
)
def test_invalid_request(payload: dict[str, object]) -> None:
    response = client.post("/predict", json=payload)

    assert response.status_code == 422
    assert response.headers["content-type"].startswith("application/json")

    errors = response.json()["detail"]

    assert isinstance(errors, list)
    assert len(errors) > 0
    assert all("msg" in error and "loc" in error for error in errors)
