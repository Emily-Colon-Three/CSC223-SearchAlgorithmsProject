from algorithms import recursive_binary_search
from algorithms import iterative_binary_search
from algorithms import sequential_search

# Typical list tests
print ("Part 1: Typical List")
normal_list = [1, 3, 5, 7, 11, 13, 17, 19, 23]
middle = 11
beginning = 1
end = 23
absent = 4
print("Target Indices: 4, 0, 8, Absent (-1)")

# Recursive Binary Search Results
print("Recursive Binary Search:")
print(recursive_binary_search(normal_list, middle, 0, len(normal_list) - 1))
print(recursive_binary_search(normal_list, beginning, 0, len(normal_list) - 1))
print(recursive_binary_search(normal_list, end, 0, len(normal_list) - 1))
print(recursive_binary_search(normal_list, absent, 0, len(normal_list) - 1), '\n')

# Iterative Binary Search Results
print("Iterative Binary Search:")
print(iterative_binary_search(normal_list, middle))
print(iterative_binary_search(normal_list, beginning))
print(iterative_binary_search(normal_list, end))
print(iterative_binary_search(normal_list, absent), '\n')

# Sequential Search Results
print("Sequential Search:")
print(sequential_search(normal_list, middle))
print(sequential_search(normal_list, beginning))
print(sequential_search(normal_list, end))
print(sequential_search(normal_list, absent), '\n')


# Single-element list tests
print("Part 2: Single Element")
single_list = [1]
present = 1
absent = 0
print("Target Indices: 0, Absent (-1)")

# Recursive Binary Results
print("Recursive Binary Search:")
print(recursive_binary_search(single_list, present, 0, len(single_list) - 1))
print(recursive_binary_search(single_list, absent, 0, len(single_list) - 1), '\n')

# Iterative Binary Results
print("Iterative Binary Search:")
print(iterative_binary_search(single_list, present))
print(iterative_binary_search(single_list, absent), '\n')

# Sequential Results
print("Sequential Search:")
print(sequential_search(single_list, present))
print(sequential_search(single_list, absent), '\n')


# Empty List Test
print("Part 3: Empty List")
empty = []
absent = 0
print("Target Index: Absent (-1)")

print("Recursive Binary Search:")
print(recursive_binary_search(empty, absent, 0, len(empty) - 1), '\n')

print("Iterative Binary Search:")
print(recursive_binary_search(empty, absent, 0, len(empty) - 1), '\n')

print("Sequential Search:")
print(sequential_search(empty, absent), '\n')


# Duplicates List tests
print("Part 4: List of Duplicates")
duplicates = [2, 2, 2, 4, 4, 4, 4, 4, 6, 6, 8, 8, 8, 10, 10, 12, 12, 12, 12, 12, 12]
present = 10
absent = 9
print("Target Indices: 13 or 14, Absent (-1)")

# Recursive Binary
print("Recursive Binary Search:")
print(recursive_binary_search(duplicates, present, 0, len(duplicates) - 1))
print(recursive_binary_search(duplicates, absent, 0, len(duplicates) - 1), '\n')

# Iterative Binary
print("Iterative Binary Search:")
print(iterative_binary_search(duplicates, present))
print(iterative_binary_search(duplicates, absent), '\n')

# Sequential
print("Sequential Search:")
print(sequential_search(duplicates, present))
print(sequential_search(duplicates, absent), '\n')