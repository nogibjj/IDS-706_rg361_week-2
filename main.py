""" Function to return the descriptive statistics of a Pandas Dataframe"""
import pandas as pd


def descriptive_stats(fname, col=None):
    df = pd.read_csv(fname)

    if col == None:
        col = len(df.axes[1]) - 1
    else:
        col = col - 1

    return [df.iloc[:, col].mean(), df.iloc[:, col].median(), df.iloc[:, col].std()]
