# imports
import numpy as np


# evaluation
def mean_absolute_percentage_error(y_true, y_pred): 
    return np.mean(np.abs((y_true - y_pred) / y_true)) * 100



# prediction "models"
def moving_average(series, n):
    """
        Calculate average of last n observations
        Can predict 1 future value
    """
    return np.average(series[-n:])
