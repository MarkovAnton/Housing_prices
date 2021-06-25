def change_data(full_df):
    full_df['GarageCars'] = full_df['GarageCars'].apply(int)
    full_df['BsmtHalfBath'] = full_df['BsmtHalfBath'].astype(int)
    full_df['BsmtFullBath'] = full_df['BsmtFullBath'].astype(int)
    full_df['GarageCars'] = full_df['GarageCars'].apply(str)
    full_df['BsmtHalfBath'] = full_df['BsmtHalfBath'].astype(str)
    full_df['BsmtFullBath'] = full_df['BsmtFullBath'].astype(str)
    full_df['YrSold'] = full_df['YrSold'].astype(str)
    full_df['MoSold'] = full_df['MoSold'].astype(str)
    full_df['MSSubClass'] = full_df['MSSubClass'].apply(str)
    full_df['OverallCond'] = full_df['OverallCond'].astype(str)
    full_df['TotRmsAbvGrd'] = full_df['TotRmsAbvGrd'].astype(str)

    return full_df

