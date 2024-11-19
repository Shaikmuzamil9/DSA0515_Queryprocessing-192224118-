import pandas as pd
import numpy as np

# Create a DataFrame with random values
np.random.seed(0)  # For reproducibility
df = pd.DataFrame(np.random.rand(10, 4), columns=['A', 'B', 'C', 'D'])

styled_df = df.style.set_properties(**{
    'background-color': 'black',
    'color': 'yellow'
})

styled_df
