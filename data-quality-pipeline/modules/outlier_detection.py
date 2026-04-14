import numpy as np
from scipy import stats

def remove_outliers(data):

    numeric_data = data.select_dtypes(include=[np.number])

    if numeric_data.shape[1] == 0:
        return data

    z_scores = np.abs(stats.zscore(numeric_data, nan_policy='omit'))
    data = data[(z_scores < 3).all(axis=1)]

    return data