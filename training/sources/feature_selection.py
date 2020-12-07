from sklearn.feature_selection import SelectKBest, f_regression, f_classif
import pandas as pd

def filter_numeric_feature(X, y, k=10):
    '''
    Given X and y, returns a DataFrame with the features selected and their pearsons' score.
    Additionally, k represent the number of top features to select, the "all" option 
    bypasses selection, for use in a parameter search.
    '''
    #feature selection using f_regression 
    fs = SelectKBest(score_func=f_regression, k=k)
    fit = fs.fit(X,y)
    #create df for scores
    dfscores = pd.DataFrame(fit.scores_)
    #create df for column names
    dfcolumns = pd.DataFrame(X.columns)
    #concat two dataframes for better visualization 
    featureScores = pd.concat([dfcolumns,dfscores],axis=1)
    #naming the dataframe columns
    featureScores.columns = ['selected_columns','score_pearsons']
    return featureScores.sort_values(by='score_pearsons', ascending=False)

def filter_categorical_feature(X, y, k=10):
    '''
    Given X and y, returns a DataFrame with the features selected and their ANOVA's score.
    Additionally, k represent the number of top features to select, the "all" option 
    bypasses selection, for use in a parameter search.
    '''
    #feature selection using f_classif
    fs = SelectKBest(score_func=f_classif, k=k)
    fit = fs.fit(X,y)
    #create df for scores
    dfscores = pd.DataFrame(fit.scores_)
    #create df for column names
    dfcolumns = pd.DataFrame(X.columns)
    #concat two dataframes for better visualization 
    featureScores = pd.concat([dfcolumns,dfscores],axis=1)
    #naming the dataframe columns
    featureScores.columns = ['selected_columns','score_ANOVA']
    return featureScores.sort_values(by='score_ANOVA', ascending=False)