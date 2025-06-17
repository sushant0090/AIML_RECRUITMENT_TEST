
import pandas as pd
import re

def process_text(df):
    df['text'] = df['text'].str.lower()
    df['text'] = df['text'].apply(lambda x: re.sub(r'[^a-z0-9\s]', '', x))
    df['text'] = df['text'].apply(lambda x: x.split())
    return df

data = {
    'text': ['Hello World!', 'Python@Rocks', 'Text#Data!!']
}

df = pd.DataFrame(data)
df = process_text(df)
print(df)