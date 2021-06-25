def clear_num_features(full_df):
    num_col_na = ['BsmtFinSF1', 'BsmtFinSF2', 'BsmtUnfSF', 'TotalBsmtSF',
                  'BsmtFullBath', 'MasVnrArea', 'BsmtHalfBath', 'BsmtFinSF1',
                  'BsmtFinSF2', 'BsmtUnfSF', 'GarageYrBlt', 'GarageArea', 'GarageCars']

    for col in num_col_na:
        full_df[col].fillna(0, inplace=True)

    return full_df

