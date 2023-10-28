def min_value(*args):
    # initialize data
    current_min_value = None

    # determine the minimum value
    for value in args :
        if current_min_value is None :
            current_min_value = value
        elif current_min_value > value :
            current_min_value = value

    return current_min_value

def max_value(*args):
    # initialize data
    current_max_value = None

    # determine the maximum value
    for value in args :
        if current_max_value is None :
            current_max_value = value
        elif current_max_value < value :
            current_max_value = value

    return current_max_value

def average_value(*args):
    # determine the average value
    sum_values = sum(args)
    avg_value = sum_values / len(args)

    return avg_value