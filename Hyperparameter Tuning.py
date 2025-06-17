from sklearn.datasets import load_iris
from sklearn.ensemble import RandomForestClassifier
from sklearn.model_selection import GridSearchCV

def tune_random_forest():
    data = load_iris()
    X = data.data
    y = data.target

    model = RandomForestClassifier()

    params = {
        'max_depth': [3, 5, 7],
        'n_estimators': [50, 100]
    }

    grid = GridSearchCV(model, params, cv=3)
    grid.fit(X, y)

    print("Best Parameters:", grid.best_params_)
    print("Best Score:", grid.best_score_)

tune_random_forest()