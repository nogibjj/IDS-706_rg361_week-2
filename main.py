""" Function to return the descriptive statistics of a Pandas Dataframe"""
import pandas as pd

# %%
import matplotlib.pyplot as plt


def descriptive_stats(fname, col=None):
    df = pd.read_csv(fname)

    if col == None:
        col = len(df.axes[1]) - 1
    else:
        col = col - 1

    col_name = df.columns[col]

    plt.hist(df[col_name])  # .plot()
    plt.ylabel("Count of " + col_name)
    plt.xlabel(col_name)
    plt.title("Data Loaded from : " + fname)
    plt.show()
    plt.savefig("./resources/output.png")
    plt.clf()

    return [df.iloc[:, col].mean(), df.iloc[:, col].median(), df.iloc[:, col].std()]
