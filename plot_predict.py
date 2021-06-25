import seaborn as sns
import matplotlib.pyplot as plt
from IPython.core.pylabtools import figsize


def plot_pred(final_pred, test_y):
    figsize(8, 8)

    # Density plot of the final predictions and the test values
    sns.kdeplot(final_pred, label='Predictions')
    sns.kdeplot(test_y, label='Values')

    # Label the plot
    plt.xlabel('Energy Star Score')
    plt.ylabel('Density')
    plt.title('Test Values and Predictions')
    plt.legend()
    plt.show()

