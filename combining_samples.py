import pandas as pd


def combine_samples(train, test):
    full_df = pd.concat([train.iloc[:, 0:], test.iloc[:, 0:]])
    return full_df

