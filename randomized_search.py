from sklearn.model_selection import RandomizedSearchCV
from sklearn.ensemble import GradientBoostingRegressor


def random_search(hyperparameter_grid):
    # Create the model to use for hyperparameter tuning
    model = GradientBoostingRegressor(random_state=2021)

    # Set up the random search with 4-fold cross validation
    random_cv = RandomizedSearchCV(estimator=model,
                                   param_distributions=hyperparameter_grid,
                                   cv=4, n_iter=25,
                                   scoring='neg_mean_absolute_error',
                                   n_jobs=-1, verbose=1,
                                   return_train_score=True,
                                   random_state=42)

    return random_cv

