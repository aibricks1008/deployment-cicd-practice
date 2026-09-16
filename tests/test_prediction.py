from pathlib import Path
import joblib
from sklearn.ensemble import RandomForestClassifier
from src.predict import predict
from src.preprocessing import load_data


def test_model_can_be_trained_loaded_and_predicts(tmp_path: Path):
    features, labels = load_data()
    model = RandomForestClassifier(n_estimators=5, random_state=42).fit(features, labels)
    model_path = tmp_path / "model.joblib"
    joblib.dump(model, model_path)
    result = predict([[5.1, 3.5, 1.4, 0.2]], model_path)
    assert result.shape == (1,)
    assert int(result[0]) in {0, 1, 2}
