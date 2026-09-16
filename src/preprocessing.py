"""Reusable preprocessing helpers for the Iris classification example."""

from typing import Tuple
import numpy as np
from sklearn.datasets import load_iris
from sklearn.model_selection import train_test_split


def load_data() -> Tuple[np.ndarray, np.ndarray]:
    """Load Iris features and labels from scikit-learn."""
    dataset = load_iris()
    return dataset.data, dataset.target


def split_data(features, labels, test_size=0.2, random_state=42):
    """Create reproducible stratified training and test splits."""
    return train_test_split(features, labels, test_size=test_size,
                            random_state=random_state, stratify=labels)
