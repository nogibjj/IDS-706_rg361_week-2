""" Function to return the descriptive statistics of a Pandas Dataframe"""

def descriptive_stats(df, col=None):
    if col == None:
        col = len(df.axes[1])-1
    else:
        col = col -1

    return df.iloc[:, col].mean()
