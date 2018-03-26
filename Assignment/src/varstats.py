import math
from firebase import firebase
from firebase_connect import *
from assignment_file import *

def get_duration():
    duration_list = []
    for assignment in assignment_name:
        process_list = firebase.get(assignment, None)
        for item in process_list:
            each_process = process_list[item]
            if (item == 'summary' or item == 'varstats'):
                continue
            else:
                duration = each_process['Duration']
                #print(duration)
                duration_list.append(duration)
    return duration_list

def min_max(duration_list):
    return [duration_list[0], duration_list[len(duration_list) - 1]]
    #min = duration_list[0]
    #max = duration_list[0]
    #for duration in duration_list:
    #    if (duration > max):
    #        max = duration
    #    if (duration < min):
    #        min = duration
    #return [min, max]

def median(duration_list):
    lenght = len(duration_list)
    lenght = int(lenght / 2)
    if (lenght % 2 == 0):
        return (duration_list[lenght] + duration_list[lenght - 1]) / 2
    else:
        return duration_list[lenght]

def average(duration_list):
    summation = 0
    lenght = len(duration_list)
    for duration in duration_list:
        summation = summation + duration
    return summation / lenght

def standard_deviation(duration_list):
    average_val = average(duration_list)
    lenght = len(duration_list)
    summation = 0
    for duration in duration_list:
        summation = summation + ((duration - average_val) * (duration - average_val))
    stdev = math.sqrt(summation / lenght)
    return stdev

def quartile(duration_list):
    quartile_list = []
    lenght = len(duration_list)
    #print(lenght)
    for i in range(1, 4, 1):
        index = (i / 4) * (lenght + 1)
        #print(index, int(index), index - int(index))
        if (index - int(index) == 0.0):
            quartile_val = duration_list[int(index) - 1]
            quartile_list.append(quartile_val)
        else:
            diff = index - int(index)
            #print(diff)
            quartile_val = duration_list[int(index) - 1] + (diff * (duration_list[int(index)] - duration_list[int(index) - 1]))
            quartile_list.append(quartile_val)
        #print(index, quartile_val)

    return quartile_list

def percentile(duration_list):
    percentile_list = []
    lenght = len(duration_list)
    for i in range(10, 100, 10):
        index = (i / 100) * (lenght + 1)
        if (index - int(index) == 0.0):
            percentile_val = duration_list[int(index) - 1]
            percentile_list.append(percentile_val)
        else:
            diff = index - int(index)
            percentile_val = duration_list[int(index) - 1] + (diff * (duration_list[int(index)] - duration_list[int(index) - 1]))
            percentile_list.append(percentile_val)
    return percentile_list

def avg_and_sigma(average_val, stdev_val):
    avg_and_sigma_list = []
    for i in range (-2, 3, 1):
        result = average_val + ((i)*stdev_val)
        avg_and_sigma_list.append(result)
    return avg_and_sigma_list

def log_of_avg_and_sigma(avg_and_sigma_val):
    log_of_avg_and_sigma_list = []
    for item in avg_and_sigma_val:
        #result = item * item
        if (item < 0):
            result = item * (-1)
        else:
            result = item
        result = math.log(result, 10)
        log_of_avg_and_sigma_list.append(result)
    return log_of_avg_and_sigma_list

def to_expo(log_of_avg_and_sigma_val):
    to_expo_list = []
    for item in log_of_avg_and_sigma_val:
        to_expo_list.append(10**item)
    return to_expo_list


def post_varstat_to_firebase():
    duration_list = get_duration()
    duration_list.sort()

    min_max_val = min_max(duration_list)
    median_val = median(duration_list)
    average_val = average(duration_list)
    stdev_val = standard_deviation(duration_list)
    quartile_val = quartile(duration_list)
    percentile_val = percentile(duration_list)

    avg_and_sigma_val = avg_and_sigma(average_val, stdev_val)
    log_of_avg_and_sigma_val = log_of_avg_and_sigma(avg_and_sigma_val)
    to_expo_val = to_expo(log_of_avg_and_sigma_val)

    #print(duration_list)
    #print(min_max_val)
    #print(median_val)
    #print(average_val)
    #print(stdev_val)
    #print(quartile_val)
    #print(percentile_val)
    #print(avg_and_sigma_val)
    #print(log_of_avg_and_sigma_val)
    #print(to_expo_val)

    varstats_data = {'Duration list': duration_list, 
                     'Min': min_max_val[0], 
                     'Max': min_max_val[1], 
                     'Median': median_val, 
                     'Average': average_val, 
                     'Standard Deviation': stdev_val, 
                     'Quartile': quartile_val, 
                     'Percentile': percentile_val, 
                     'Average + nStdev': avg_and_sigma_val, 
                     'Log10(Average + nStdev)': log_of_avg_and_sigma_val, 
                     '10^Log10(Average + nStdev)' : to_expo_val}

    firebase.patch(my_url + '/all_varstats', varstats_data)


def main():
    post_varstat_to_firebase()

if __name__ == "__main__":
    main()