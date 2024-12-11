import math
from collections import Counter

def get_statistics(input_list):

    sorted_input_list = sorted(input_list)
    n = len(input_list)

    mean = sum(sorted_input_list)/n

    middle_idx = (n-1) //2

    median = sorted_input_list[middle_idx]
    if n%2==0:
        median = (sorted_input_list[middle_idx] + sorted_input_list[middle_idx+1])/2


    

    frequencies = { x: sorted_input_list.count(x) for x in set(sorted_input_list)}
    mode = max(frequencies.keys(), key=lambda num: frequencies[num])
    


    sample_variance = sum([(number-mean)**2/(n-1) for number in sorted_input_list])
    

    sample_standard_deviation = sample_variance ** 0.5



    mean_standard_error = sample_standard_deviation / n ** 0.5
    z_score_standard_error = 1.96*mean_standard_error
    mean_confidence_interval = [mean-z_score_standard_error, mean+z_score_standard_error]


    return {
        "mean": mean,
        "median": median,
        "mode": mode,
        "sample_variance": sample_variance,
        "sample_standard_deviation": sample_standard_deviation,
        "mean_confidence_interval": mean_confidence_interval,
    }




if __name__=="__main__":

    input = [2, 1, 3, 4, 4, 5, 6, 7]
    sol = get_statistics(input)
    print(sol)