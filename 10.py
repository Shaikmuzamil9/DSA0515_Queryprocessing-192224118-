
import pandas as pd
import numpy as np
np.random.seed(0)  # for reproducibility
data = np.random.randn(10, 4)  # generating random values
df = pd.DataFrame(data, columns=['A', 'B', 'C', 'D'])

styled_df = df.style.apply(lambda x: ['color: red' if val < 0 else 'color: black' for val in x])
styled_df
