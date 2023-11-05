# Solomon Falode 2154980
# Input: Read a list of integers from user
input_list = input().split()

# Convert strings to integers
input_list = [int(x) for x in input_list]

# Filtering: Get only non-negative integers
non_negatives = [x for x in input_list if x >= 0]

# Sorting: Sort the non-negative integers in ascending order
sorted_list = sorted(non_negatives)

# Output: Print the sorted list of non-negative integers
for num in sorted_list:
    print(num, end=' ')
