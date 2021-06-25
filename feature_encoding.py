from sklearn.preprocessing import LabelEncoder


def code_features(full_df, cat_features):
    for c in cat_features:
        lbl = LabelEncoder()
        full_df[c] = lbl.fit_transform(full_df[c])

    return full_df

