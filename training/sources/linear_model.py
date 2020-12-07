from sklearn.linear_model import LinearRegression, Lasso, Ridge, ElasticNet

def linear_model(X_train, X_test, y_train):
    '''
    Given X_train, X_test, y_train,
    Returns y_pred, y_pred_train, in that order as a tuple.
    Note: to train the model using all the data just do the following:
        X_train = X,
        X_test = X_pred (data from which makes predictions),
        y_train = y
    Uses sklearn LinerarRegression model.
    '''
    model = LinearRegression()
    model.fit(X_train, y_train)
    y_pred = model.predict(X_test)
    y_pred_train = model.predict(X_train)
    return y_pred, y_pred_train

def ridge_model(X_train, X_test, y_train, alpha=1, iterations=10000):
    '''
    Given X_train, X_test, y_train,
    Returns y_pred, y_pred_train, in that order as a tuple.
    Uses sklearn Ridge model.
    '''
    ridge = Ridge(alpha=alpha, max_iter=iterations)
    ridge.fit(X_train,y_train)
    y_pred = ridge.predict(X_test)
    y_pred_train = ridge.predict(X_train)
    return y_pred, y_pred_train

def lasso_model(X_train, X_test, y_train, alpha=1, iterations=10000):
    lasso = Lasso(alpha=alpha,max_iter=10000)
    lasso.fit(X_train,y_train)
    y_pred = lasso.predict(X_test)
    y_pred_train = lasso.predict(X_train)
    return y_pred, y_pred_train