"""Train and save the Iris Random Forest classifier."""
from pathlib import Path
import joblib
import yaml
from sklearn.ensemble import RandomForestClassifier
from sklearn.metrics import accuracy_score
from src.preprocessing import load_data, split_data

ROOT = Path(__file__).resolve().parents[1]


def train_model(config_path=ROOT / "configs" / "config.yaml"):
    with config_path.open(encoding="utf-8") as file:
        config = yaml.safe_load(file)
    features, labels = load_data()
    x_train, x_test, y_train, y_test = split_data(
        features, labels, config["test_size"], config["random_state"])
    model = RandomForestClassifier(n_estimators=config["n_estimators"],
                                   random_state=config["random_state"])
    model.fit(x_train, y_train)
    accuracy = accuracy_score(y_test, model.predict(x_test))
    model_path = ROOT / config["model_path"]
    model_path.parent.mkdir(parents=True, exist_ok=True)
    joblib.dump(model, model_path)
    return accuracy


if __name__ == "__main__":
    print(f"Test accuracy: {train_model():.2%}")
