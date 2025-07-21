import pandas as pd
def transform(df):
    df['price'] = pd.to_numeric(df['price'], errors='coerce').round(2)
    return df

