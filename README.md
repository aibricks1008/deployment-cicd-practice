# Simple ML CI/CD Learning Project

This small CPU-only project trains a scikit-learn `RandomForestClassifier` on the built-in Iris dataset. It is intended for learning Git, Azure Repos, Azure Pipelines, Docker, and basic MLOps workflows.

## Structure

- `src/preprocessing.py` — dataset loading and splitting helpers
- `src/train.py` — training, accuracy reporting, and model saving
- `src/predict.py` — reusable prediction function and example
- `tests/` — fast pytest checks
- `configs/config.yaml` — training configuration
- `models/model.joblib` — generated model artifact (ignored by Git)

## Windows setup

```powershell
python -m venv .venv
.\\.venv\\Scripts\\Activate.ps1
python -m pip install -r requirements.txt
```

## Train

```powershell
python -m src.train
```

This prints test accuracy and saves `models/model.joblib`.

## Predict

```powershell
python -m src.predict
```

## Test

```powershell
python -m pytest
```
## Development

This project is used to practice Git and CI/CD workflows.