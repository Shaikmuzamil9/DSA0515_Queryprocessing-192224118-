import pandas as pd
import numpy as np
data = {
    'A': [1, 2, None, 4, 5],
    'B': [None, None, None, None, None],
    'C': [1, 2, 3, 4, 5]
}
df = pd.DataFrame(data)
df.replace({None: np.nan}, inplace=True)  # Replace None with NaN
df.fillna('Unknown', inplace=True)  # Replace NaN with 'Unknown' for categorical data
print(df)
