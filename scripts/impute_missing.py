import numpy as np
import sklearn

import load_raw_csv

train_df = load_raw_csv.load_raw_csv()
# Fill single entry of Electrical feature with most common value
train_df = train_df.fillna({'Electrical':'SBrkr'})

# Of the 1460 entries in the training data, only 7 have pools.
# Current plan to convert "Pool" data into Boolean and drop original "Pool columns"
train_df['PoolBool'] = train_df['PoolArea'].apply(lambda x: 1 if x > 0 else 0)
train_df = train_df.drop(columns=['PoolArea', 'PoolQC'])

# Fill in Missing Garage Type with "None" as those homes most likely don't have Garages
train_df = train_df.fillna({'GarageType':'None'})
NaN_train_count_series = train_df.isna().sum()
print(NaN_train_count_series[NaN_train_count_series > 0])