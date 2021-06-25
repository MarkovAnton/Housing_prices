def hyperparam_list():
    # Loss function to be optimized
    loss = ['ls', 'lad', 'huber']

    # Number of trees used in the boosting process
    n_estimators = [100, 500, 900, 1000, 1500]

    # Maximum depth of each tree
    max_depth = [2, 3, 4, 5, 6, 10, 15]

    # Minimum number of samples per leaf
    min_samples_leaf = [1, 2, 4, 6, 8]

    # Minimum number of samples to split a node
    min_samples_split = [2, 4, 6, 10]

    # Maximum number of features to consider for making splits
    max_features = ['auto', 'sqrt', 'log2', None]

    # Define the grid of hyperparameters to search
    hyperparameter_grid = {'loss': loss,
                           'n_estimators': n_estimators,
                           'max_depth': max_depth,
                           'min_samples_leaf': min_samples_leaf,
                           'min_samples_split': min_samples_split,
                           'max_features': max_features}

    return hyperparameter_grid

