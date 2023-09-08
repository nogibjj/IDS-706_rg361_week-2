"""Test file to verify main function"""

import pandas as pd
from main import descriptive_stats

def test_stat():
    # initialize list elements
    name = ["A", "B", "C", "D"]
    age = [10,20,30,40]
    height = [5, 5.5, 6, 5]
      
    # Create the pandas DataFrame
    df = pd.DataFrame(list(zip(name, age, height)), columns =['Name', 'Age', 'Height'])
    
    assert df.loc[:, 'Age'].mean() == descriptive_stats(df,2)
    assert df.loc[:, 'Height'].mean() == descriptive_stats(df)

test_stat()
