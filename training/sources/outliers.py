from scipy import stats
import numpy as np
import pandas as pd

def outliers_info(feature, threshold=3):
    '''
    Given a feature column and a number that represent the Z-score.
        "The Z-score is the signed number of standard 
        deviations by which the value of an observation 
        or data point is above the mean value of what 
        is being observed or measured"
    The function returns basic info about those outliers found.
        result = {
            'feature': f'{feature}',
            'threshold': threshold,
            'number_of_outliers': len(z[outliers]),
            'outliers': z[outliers],
            'outliers_index': outliers
        }
    '''
    z = np.abs(stats.zscore(feature))
    outliers = np.where(z > threshold)
    return {
        'feature': f'{feature}',
        'threshold': threshold,
        'number_of_outliers': len(z[outliers]),
        'outliers': z[outliers],
        'outliers_index': outliers
    }

def get_outliers_quantile(feature, tail=0.05):
    '''
    Given a feature column and a percentage (0 < tail < 1), equivalent to the tail in a 
    normal distribution, the function returns the index list of outliers in the given feature.
    '''
    filt = feature.between(feature.quantile(tail), feature.quantile(1 - tail))
    print(filt.value_counts())
    return feature[~filt].index

