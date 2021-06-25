def sort_features(final_model, train_X):
    print(sorted(
        zip(train_X.columns, final_model.feature_importances_),
        key=lambda p: p[1],
        reverse=True
    ))

