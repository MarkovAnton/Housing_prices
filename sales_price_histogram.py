import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt


def sales_price_hist(train):
    plot_hist = pd.DataFrame()
    plot_hist['Sale Price'] = train['SalePrice']
    sns.histplot(data=plot_hist, x='Sale Price', bins=40)
    plt.title('SalesPrice bar chart')
    plt.show()

