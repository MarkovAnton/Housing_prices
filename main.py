import pandas as pd
from config import *
from reading_files import read_files
from sales_price_histogram import sales_price_hist
from correlations import corr_data
from sample_sizes import sample_size
from columns_information import col_info
from feature_splitting import feat_split
from combining_samples import combine_samples
from new_categorical_features import new_cat_features
from clearing_numeric_features import clear_num_features
from clearing_categorical_features import clear_cat_features
from change_data_type import change_data
from feature_encoding import code_features
from calculating_asymmetry import calc_asymmetry
from splitting_data import split_data
from hyperparameter_list import hyperparam_list
from randomized_search import random_search
from grid_search import grid_search_cv
from plotting_mean_error import plot_mean_error
from plot_predict import plot_pred
from distribution_of_residuals import distrib_of_residuals
from sorted_features import sort_features
from shap_values import shap_val
from write_to_file import write_file


def main():
    train = read_files(PATH_TRAIN, PATH_TEST)[0]
    test = read_files(PATH_TRAIN, PATH_TEST)[1]
    print(train)
    print(test)
    ntrain = len(train)
    sales_price_hist(train)
    corr_data(train)
    sample_size(train, test)
    col_info(train, test)
    num_features = feat_split()
    Y_train = train['SalePrice']
    del train['SalePrice']
    full_df = combine_samples(train, test)
    print(full_df.isnull().sum().sort_values(ascending=False).head(10))
    full_df.drop(['Alley', 'FireplaceQu', 'PoolQC', 'Fence', 'MiscFeature'], axis=1, inplace=True)
    cat_features = new_cat_features()
    full_df = clear_num_features(full_df)
    full_df = clear_cat_features(full_df)
    full_df = change_data(full_df)
    print(full_df.isnull().sum().max())
    full_df = code_features(full_df, cat_features)
    print(full_df[cat_features].head(10))
    full_df = calc_asymmetry(train, full_df, num_features)
    print(full_df.info())
    train_set = full_df[:ntrain].reset_index()
    print(train_set)
    test_set = full_df[ntrain:].reset_index()
    print(test_set)
    train_X = split_data(train_set, Y_train)[0]
    print(train_X)
    test_X = split_data(train_set, Y_train)[1]
    print(test_X)
    train_y = split_data(train_set, Y_train)[2]
    print(train_y)
    test_y = split_data(train_set, Y_train)[3]
    print(test_y)
    hyperparameter_grid = hyperparam_list()
    random_cv = random_search(hyperparameter_grid)
    random_cv.fit(train_X, train_y)
    random_results = pd.DataFrame(random_cv.cv_results_).sort_values('mean_test_score', ascending=False)
    print(random_results.head(10))
    best_estimate_cv = random_cv.best_estimator_
    print(best_estimate_cv)
    grid_search = grid_search_cv(best_estimate_cv)
    grid_search.fit(train_X, train_y)
    plot_mean_error(grid_search)
    results = pd.DataFrame(grid_search.cv_results_)
    print(results.sort_values('mean_test_score', ascending=False).head(5))
    final_model = grid_search.best_estimator_
    print(final_model)
    model_fit = final_model.fit(train_X, train_y)
    print(final_model.score(test_X, test_y))
    final_pred = final_model.predict(test_X)
    plot_pred(final_pred, test_y)
    distrib_of_residuals(final_pred, test_y)
    sort_features(final_model, train_X)
    shap_val(model_fit, train_X)
    write_file(final_model, test, test_set)


if __name__ == '__main__':
    main()

