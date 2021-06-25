import numpy as np
from scipy.stats import skew


def calc_asymmetry(train, full_df, num_features):
    skewed_feats = train[num_features].apply(lambda x: skew(x.dropna()))
    skewed_feats = skewed_feats[skewed_feats > 0.75]
    skewed_feats = skewed_feats.index
    full_df[skewed_feats] = np.log1p(full_df[skewed_feats])

    return full_df

