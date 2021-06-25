import pandas as pd


def read_files(path_train, path_test):
    train = pd.read_csv(path_train, index_col='Id')
    test = pd.read_csv(path_test, index_col='Id')
    return train, test

