import pandas as pd
import matplotlib.pyplot as plt
from IPython.core.pylabtools import figsize


def plot_mean_error(grid_search):
    plt.rcParams['font.size'] = 24
    results = pd.DataFrame(grid_search.cv_results_)

    # Plot the training and testing error vs number of trees
    figsize(8, 8)
    plt.style.use('fivethirtyeight')
    plt.plot(results['param_n_estimators'], -1 * results['mean_test_score'], label='Testing Error')
    plt.plot(results['param_n_estimators'], -1 * results['mean_train_score'], label='Training Error')
    plt.xlabel('Number of Trees')
    plt.ylabel('Mean Abosolute Error')
    plt.legend()
    plt.title('Performance vs Number of Trees')
    plt.show()

