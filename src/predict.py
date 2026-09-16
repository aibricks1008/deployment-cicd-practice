"""Load the trained model and make predictions."""
from pathlib import Path
import joblib

ROOT = Path(__file__).resolve().parents[1]


def predict(features, model_path=ROOT / "models" / "model.joblib"):
    """Return predictions for one or more rows of Iris features."""
    return joblib.load(model_path).predict(features)


if __name__ == "__main__":
    print(f"Predicted class: {predict([[5.1, 3.5, 1.4, 0.2]])[0]}")
