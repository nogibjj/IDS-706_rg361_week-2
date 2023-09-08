"""Test file to verify main function"""

import pandas as pd
from main import descriptive_stat

def test_stat():
    # initialize list elements
    data = [10,20,30,40,50,60]
      
    # Create the pandas DataFrame with column name is provided explicitly
    df = pd.DataFrame(data, columns=['Numbers'])
    
    assert df.describe == descriptive_stat(df)

test_stat()
