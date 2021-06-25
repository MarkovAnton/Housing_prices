def clear_cat_features(full_df):
    cat_col_na = ['MasVnrType', 'BsmtCond', 'BsmtExposure', 'BsmtQual', 'BsmtFinType1', 'BsmtFinType2', 'MasVnrType',
                  'GarageFinish', 'GarageType', 'GarageCond', 'GarageQual']

    for col in cat_col_na:
        full_df[col].fillna('Others', inplace=True)

    full_df['Functional'].fillna('Typ', inplace=True)
    full_df['Electrical'].fillna('SBrkr', inplace=True)
    full_df['SaleType'].fillna('Oth', inplace=True)
    full_df['KitchenQual'].fillna('TA', inplace=True)
    full_df['SaleType'].fillna('Oth', inplace=True)
    full_df['Exterior1st'].fillna('Other', inplace=True)
    full_df['Exterior2nd'].fillna('Other', inplace=True)
    full_df['Utilities'].fillna('AllPub', inplace=True)

    lotfrontage_by_neighborhood = full_df.groupby('Neighborhood')['LotFrontage'].median()

    for ngh in lotfrontage_by_neighborhood.index:
        full_df.loc[(full_df['LotFrontage'].isnull()) & (full_df['Neighborhood'] == ngh), ['LotFrontage']] = \
        lotfrontage_by_neighborhood[ngh]

    full_df['MSZoning'] = full_df['MSZoning'].transform(lambda x: x.fillna(x.mode()[0]))

    remap = {180: 1, 30: 1, 45: 1, 190: 2, 50: 2, 90: 2, 85: 2, 40: 2, 160: 2, 70: 3, 20: 3, 75: 3, 80: 3, 120: 4,
             60: 5}
    full_df['MSSubClass'].replace(remap, inplace=True)

    return full_df

