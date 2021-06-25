import matplotlib.pyplot as plt


def distrib_of_residuals(final_pred, test_y):
    # Calculate the residuals
    residuals = final_pred - test_y

    # Plot the residuals in a histogram
    plt.hist(residuals, color='red', bins=20,
             edgecolor='black')
    plt.xlabel('Error')
    plt.ylabel('Count')
    plt.title('Distribution of Residuals')
    plt.show()

