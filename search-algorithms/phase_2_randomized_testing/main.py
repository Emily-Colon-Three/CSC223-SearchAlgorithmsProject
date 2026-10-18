import random
from algorithms import recursive_binary_search
from algorithms import iterative_binary_search
from algorithms import sequential_search

# Random list creation
print("Random List Elements:")
random_list = [
    random.randint(1, 100)
    for _ in range(20)
]
random_list.sort() # Sorts the list so that binary searches can work on it

print(random_list) # Displays the list and its elements to user

# Defines a function which contrasts a returned index with the expected result of a search
# Returns a boolean value which is used to mark whether a return matches expected behavior.
def check_behavior(i, expectation) -> bool:
    if expectation:
        if i != -1:
            print("Target Found (Expected)")
            return True
        else:
            print("Failed to Locate Target (Unexpected)")
            return False
    else:
        if i == -1:
            print("Target Not Found (Expected)")
            return True
        else:
            print("Located Target (Unexpected)")
            return False

print("Randomized Testing:\n")
# Makes a loop which continues repeating randomized testing until cont set to True
cont = True
while cont == True:
    if random.random() < 0.5:
        target = random.choice(random_list)
        expected_present = True
    else:
        target = 101
        expected_present = False

    print("Selected Target: ", target)

    # Three search algorithms now have to return target index

    print("Recursive Binary Search:")
    index = recursive_binary_search(random_list, target, 0, len(random_list) - 1)
    recursive = check_behavior(index, expected_present)
    print("Index Returned: ", index)

    print("Iterative Binary Search:")
    index = iterative_binary_search(random_list, target)
    iterative = check_behavior(index, expected_present)
    print("Index Returned: ", index)

    print("Sequential Binary Search:")
    index = sequential_search(random_list, target)
    sequential = check_behavior(index, expected_present)
    print("Index Returned: ", index)

    # Message for whether results acceptable
    if recursive & iterative & sequential:
        print("All Results Acceptable.\n")

    cont = input("Continue? (1): ") # Prompts user for whether they will run another round