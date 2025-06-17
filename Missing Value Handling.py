import pandas as pd
import numpy as np

def handle_missing_income(df):
    skew = df['income'].skew()
    if abs(skew) <= 0.5:
        value = df['income'].median()
        df['income'] = df['income'].fillna(value)
        print("Filled with median:", value)
    else:
        value = df['income'].mode()[0]
        df['income'] = df['income'].fillna(value)
        print("Filled with mode:", value)
    return df

data = {
    'name': ['A', 'B', 'C', 'D', 'E'],
    'income': [1000, 2000, np.nan, 1500, np.nan]
}

df = pd.DataFrame(data)
df = handle_missing_income(df)
print(df)