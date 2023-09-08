""" Function to return the descriptive statistics of a Pandas Dataframe"""

def descriptive_stats(df, col=None):
    if col == None:
        col = len(df.axes[1])-1
        pass
    return df.iloc[:, col].mean()
