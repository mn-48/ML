
def get_statistics(input_list):
    # Write your code here.
    return {
        "mean": 0,
        "median": 0,
        "mode": 0,
        "sample_variance": 0,
        "sample_standard_deviation": 0,
        "mean_confidence_interval": [0, 0],
    }




if __name__=="__main__":

    input = [2, 1, 3, 4, 4, 5, 6, 7]
    sol = get_statistics(input)
    print(sol)