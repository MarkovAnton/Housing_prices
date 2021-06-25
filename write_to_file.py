import pandas as pd


def write_file(final_model, test, test_set):
    result = pd.DataFrame()
    result['Id'] = test.index
    result['SalePrice'] = final_model.predict(test_set)
    result.to_csv('submission.csv', index=False)

