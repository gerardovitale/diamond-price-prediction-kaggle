from sklearn.preprocessing import normalize, StandardScaler
import pandas as pd
import numpy as np

def normalization(feature):
    '''
    Normalizes a given feature, using sklearn.preprocessing.normalize
    Returns a vector (numpy array) with the values normalized.
    '''
    normalized_X = normalize([np.array(feature)])
    return normalized_X[0]

def normalizing_df(df):
    '''
    Normalizes a complete DataFrame, feature per feature.
    Takes advantage of the normalization function.
    Returns the DataFrame normalized.
    '''
    features = df.columns
    for x in features:
        df[x] = normalization(df[x])
    return df
    
def standardizing_df(df):
    '''
    Given a DataFrame, returns the complete df standardized,
    using sklearn.preprocessing.StandardScaler
    '''
    # Get column names first
    names = df.columns
    # Create the Scaler object
    scaler = StandardScaler()
    # Fit the data on the scaler object
    scale = scaler.fit_transform(df)
    return pd.DataFrame(scale, columns=names)