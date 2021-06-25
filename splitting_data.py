from sklearn.model_selection import train_test_split


def split_data(train_set, Y_train):
    train_X, test_X, train_y, test_y = train_test_split(
        train_set,
        Y_train,
        test_size=0.2,
        random_state=2021
    )
    return train_X, test_X, train_y, test_y

