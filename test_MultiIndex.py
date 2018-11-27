import pandas as pd
import numpy as np

def make_df(cols, ind):
    data = {c: [i for i in ind] for c in cols}
    return pd.DataFrame(data, ind)

columns = pd.MultiIndex.from_product([['Cash Rate', 'Spot Rate'],['Buying', 'Selling']], names = ['CC','Currency'])

df = make_df(columns, range(10))
print(df)





