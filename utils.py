import numpy as np
import random


# Generates num_samples samples between start_range and end_range (not inclusive of end_range)
# the cast function is run on the outputs. This can be used to specify if we want floats, ints, etc
# Example inputs: (10, 100, 2, int)
# Example output: (25,60)
def RandomSamples(start_range, end_range, num_samples, cast_function):
    res=[]
    for i in range(num_samples):
        res+=[cast_function(random.uniform(start_range,end_range))]
    return res


# Generates equidistant samples from start_range to end_range (both inclusive)
# The samples have the difference of sample_distance.
# Example Input: (2,3,0.5)
# Example outputs: (2,2.5,3)
def GenerateSpacedSamples(start_range, end_range, sample_distance):
    return np.arange(start_range, end_range + sample_distance, sample_distance)


# Generates equidistant samples from start_range to end_range (both inclusive)
# The number of samples is num_samples
# Example inputs: (2,3,3)
# Example outputs: [2,2.5,3]

def GenerateSpacedSamples_Num(start_range, end_range, num_samples,end_inclusive=True):
    return np.linspace(start_range, end_range, num_samples, endpoint=end_inclusive)


# Generate array with length num_samples
# Each member of the array is a member of possible_choices
# Repetition is allowed, and the outputs are unordered
# Example input: possible_choices=['433','442','4312','532','523'], num_samples=4
# Example output: ['442','433','433','523']
def GenerateRandomChoices(possible_choices, num_samples):
    res = []
    for i in range(num_samples):
        res += random.sample(possible_choices,1)
    return res


# Generates list of arrays, each with length sample_length
# Each member of each sample is a value between possible_choices
# Each sample is unordered and non-repeating
# example input: possible_choices=[1,2,3,4,5], num_samples=2, sample_length=3
# example output: [[1,3,5],[5,2,4]
def GenerateRandomArrays(possible_choices, num_samples, sample_length):
    res = []
    for i in range(num_samples):
        res += [random.sample(possible_choices, sample_length)]
    return res


if __name__=="__main__":
    print(GenerateRandomArrays(possible_choices=['433','442','4312','532','523'], num_samples=2, sample_length=3))
    print(GenerateRandomChoices(possible_choices=['433','442','4312','532','523'], num_samples=4))
    print(GenerateSpacedSamples(1,10,1))
    print(GenerateSpacedSamples_Num(1, 10, 4 ))
    print(RandomSamples(10,100,5,int))