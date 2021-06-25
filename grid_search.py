from sklearn.ensemble import GradientBoostingRegressor
from sklearn.model_selection import GridSearchCV


def grid_search_cv(model):
    trees_grid = {'n_estimators': [1100, 1200, 1300, 1400, 1500, 1600, 1700, 1800]}

    # Grid Search Object using the trees range and the random forest model
    grid_search = GridSearchCV(estimator=model, param_grid=trees_grid, cv=4,
                               scoring='neg_mean_absolute_error', verbose=1,
                               n_jobs=-1, return_train_score=True)

    return grid_search

