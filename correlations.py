import seaborn as sns
import matplotlib.pyplot as plt
from IPython.core.pylabtools import figsize


def corr_data(train):
    figsize(8, 12)
    heatmap = sns.heatmap(train.corr()[['SalePrice']].sort_values('SalePrice', ascending=False), vmin=-1, vmax=1,
                          annot=True, cmap='BrBG')

    heatmap.set_title('Features Correlating with Sales Price', fontdict={'fontsize': 18}, pad=16)
    plt.show()

