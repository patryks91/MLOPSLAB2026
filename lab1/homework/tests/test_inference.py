import pytest

from inference import SentimentModel


@pytest.fixture(scope="module")
def model() -> SentimentModel:
    return SentimentModel()


def test_model_loaded(model: SentimentModel) -> None:
    assert model.classifier.n_features_in_ == 384
    assert list(model.classifier.classes_) == [0, 1, 2]


@pytest.mark.parametrize(
    "text",
    [
        "I love this product, it is wonderful!",
        "The package arrived today.",
        "This is terrible, I am very disappointed.",
    ],
)
def test_inference(model: SentimentModel, text: str) -> None:
    prediction = model.predict(text)

    assert prediction in {"negative", "neutral", "positive"}
