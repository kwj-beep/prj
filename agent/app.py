# %% [markdown]
# # import 

# %%
import pandas as pd
import numpy as np
from tabpfn import TabPFNRegressor
from importlib import resources
import os


# %%
def get_df():
    pkl=resources.files('agent').joinpath('df_fs.pkl')
    df=pd.read_pickle(pkl)
    return df

# get_df()

# %%
def fit():
    m=TabPFNRegressor()
    return 1


# fit()


