from src.preprocessing import load_data, split_data


def test_load_data_and_split():
    features, labels = load_data()
    assert features.shape == (150, 4)
    assert labels.shape == (150,)
    x_train, x_test, y_train, y_test = split_data(features, labels, 0.2, 42)
    assert len(x_train) == len(y_train) == 120
    assert len(x_test) == len(y_test) == 30
