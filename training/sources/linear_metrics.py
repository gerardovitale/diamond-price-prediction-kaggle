from sklearn.metrics import r2_score, mean_squared_error, mean_absolute_error
import csv

def linear_metrics(y_test, y_pred, model):
    '''
    Given a y_test and a y_pred, performs and returns, as a dictionary, the following calculation:
        - r2 score
        - mean squared error
        - root mean squared error
        - mean absolute error
    Note that is possible to identify the metrics with a model name (model='model_name').
    '''
    return {
        'model': model,
        'r2_score': r2_score(y_test, y_pred),
        'mean_squared_error': mean_squared_error(y_test, y_pred),
        'root_mean_squared_error': mean_squared_error(y_test, y_pred) ** 0.5,
        'mean_absolute_error': mean_absolute_error(y_test, y_pred)
    }

def save_linear_metrics(score=None, y_test=None, y_pred=None, model=None):
    if y_pred != None and y_test != None:
        score = linear_metrics(y_test, y_pred, model)
    try:
        file_name = '../outputs/scores.csv'
        with open(file_name, 'a+', newline='\r\n') as write_obj:
            # Create a writer object from csv module
            dict_writer = csv.DictWriter(write_obj, fieldnames=score.keys())
            # Add dictionary as wor in the csv
            dict_writer.writerow(score.values())
    except:
        print('it should be provided either a score or y_test, y_pred, model')

        