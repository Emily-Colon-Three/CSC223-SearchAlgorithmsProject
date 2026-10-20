from algorithms import recursive_binary_search
from algorithms import iterative_binary_search
from algorithms import sequential_search
import random
import time

data_sizes = [5_000, 50_000, 100_000, 150_000, 1_000_000]
total_trials = 10

# Simple funtion which checks if a given target is in the list, asserting whether that it is the case.
def verify_presence(list, index, target):
    if index != -1:
        assert list[index] == target
    else:
        assert target not in list

# Function which finds the median value of a numerical list
def find_median(values) -> int | float:
    if len(values) % 2 == 1: # For odd-length lists
        return values[len(values) // 2]
    else: # for even-length list
        return (values[len(values) // 2 - 1] + values[len(values) // 2]) / 2

# Outer loop, for going through each data size
for size in data_sizes:
    print("Data Size: ", size, '\n')

    # Totals for processing time across three algorithms
    times_recursive = []
    times_iterative = []
    times_sequential = []

    for i in range(total_trials): # Trial Loop
        print("Trial #", i + 1) # Add 1 to account for 0-based index

        # Creates data of specific size
        data = sorted(
            random.randint(1, size) # Input size serves as the max of the range
            for _ in range(size)
        )

        # Determining target; decides whether it will be present or absent in data
        if random.random() < 0.5:
            target = random.choice(data)
        else:
            target = size + 1 # Sets absent target to 1 above maximum possible value

        # Recursive Binary
        start = time.perf_counter()
        index_r = recursive_binary_search(data, target, 0, size - 1)
        time_elapsed = (time.perf_counter() - start) * 1_000_000 # Puts time in microseconds

        times_recursive.append(time_elapsed)
        print("Recursive Binary Time (microseconds): ", time_elapsed)

        # Iterative Binary
        start = time.perf_counter()
        index_i = iterative_binary_search(data, target)
        time_elapsed = (time.perf_counter() - start) * 1_000_000

        times_iterative.append(time_elapsed)
        print("Iterative Binary Time (microseconds): ", time_elapsed)

        # Sequential
        start = time.perf_counter()
        index_s = sequential_search(data, target)
        time_elapsed = (time.perf_counter() - start) * 1_000_000

        times_sequential.append(time_elapsed)
        print("Sequential Binary Time (microseconds): ", time_elapsed)

        # Verifies that all searches correctly identified target, present or not
        verify_presence(data, index_r, target)
        verify_presence(data, index_i, target)
        verify_presence(data, index_s, target)

    # Ensures all time arrays are sorted before medians are found
    times_recursive.sort()
    times_iterative.sort()
    times_sequential.sort()

    # Displays the median times across the ten trials for each of the three searches
    print('\n')
    print("Median Times (microseconds):")
    print("Recursive Binary: ", find_median(times_recursive))
    print("Iterative Binary: ", find_median(times_iterative))
    print("Sequential: ", find_median(times_sequential))
    print('\n')