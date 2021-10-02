import pandas as pd
from sklearn.metrics import mean_absolute_error
from sklearn.model_selection import train_test_split
from sklearn.tree import DecisionTreeRegressor


# fit
def train(length_tree, train_X, train_y):
    model_regression_train = DecisionTreeRegressor(max_leaf_nodes=length_tree, random_state=10)

    model_regression_train.fit(train_X, train_y)

    return model_regression_train


def predict(model_regression_predict, numbers):
    return model_regression_predict.predict(numbers)


def mean(result, val_y):
    return mean_absolute_error(val_y, result)


def main(csv_path="data/dataset.csv"):
    csv_data = csv_path
    data = pd.read_csv(csv_data)
    features = ["i", "j", "operation"]

    y = data.result
    X = data[features]

    train_X, val_X, train_y, val_y = train_test_split(X, y, random_state=10)

    predictions_concluded = []

    range_for_test = int(len(y) / 2)
    for i in range(2, range_for_test + 100):
        model_regression = train(i, train_X, train_y)
        predicted_result = predict(model_regression, val_X)
        mean_value = mean(predicted_result, val_y)
        predictions_concluded.append({"number": i, "result": mean_value})

    minimum = min(predictions_concluded, key=lambda x: x['result'])

    print(minimum)

    result_model = train(minimum.get("number"), train_X, train_y)
    predicted_result = predict(result_model, val_X)

    print("real ", val_y.head().tolist())
    print("predicted ", predicted_result)
    print("expected test [-1, -3, 3, -1] and got: ",
          predict(result_model, [[1, -2, 0], [-1, 2, 1], [1, 2, 0], [1, 2, 1]]))
