import shap
import matplotlib.pyplot as plt


def shap_val(model_fit, train_X):
    shap_values = shap.TreeExplainer(model_fit).shap_values(train_X)
    print(shap_values.shape)
    shap.summary_plot(shap_values, train_X)
    plt.show()

