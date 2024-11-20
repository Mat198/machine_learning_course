#!/usr/bin/python

def outlierCleaner(predictions, ages, net_worths):
    """
        Clean away the 10% of points that have the largest
        residual errors (difference between the prediction
        and the actual net worth).

        Return a list of tuples named cleaned_data where 
        each tuple is of the form (age, net_worth, error).
    """
    
    cleaned_data = []
    data = []
    for i in range(0,len(predictions)):
        error = abs(predictions[i] - net_worths[i])
        data.append((ages[i], net_worths[i], error))
    
    # Sort based on error
    data.sort(key=lambda x: x[2][0])

    size = int(0.9 * len(data))
    cleaned_data = data[0:size]
    return cleaned_data

