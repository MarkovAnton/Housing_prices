def col_info(train, test):
    print(train.columns, test.columns)
    print(train.head(), test.head())
    print(train.describe())
    print(train.info(), test.info())

