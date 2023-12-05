# Solomon Falode 2154980
# Global variable
num_calls = 0

# Partitioning algorithm
def partition(user_ids, i, k):
    # Select the middle element as the pivot
    pivot_index = (i + k) // 2
    pivot_value = user_ids[pivot_index]

    # Initialize index variables
    l = i
    h = k

    while True:
        # Find element on the left side greater than the pivot
        while user_ids[l] < pivot_value:
            l += 1

        # Find element on the right side smaller than the pivot
        while user_ids[h] > pivot_value:
            h -= 1

        # If the indexes crossed, the partitioning is done
        if l >= h:
            return h

        # Swap the elements at indexes l and h
        user_ids[l], user_ids[h] = user_ids[h], user_ids[l]

        # Move the indexes towards the center
        l += 1
        h -= 1

# Quicksort algorithm
def quicksort(user_ids, i, k):
    global num_calls
    num_calls += 1

    if i < k:
        # Partition the list
        partition_index = partition(user_ids, i, k)

        # Recursively sort the low and high partitions
        quicksort(user_ids, i, partition_index)
        quicksort(user_ids, partition_index + 1, k)


if __name__ == "__main__":
    user_ids = []
    user_id = input()
    while user_id != "-1":
        user_ids.append(user_id)
        user_id = input()

    # Initial call to quicksort
    quicksort(user_ids, 0, len(user_ids) - 1)

    # Print number of calls to quicksort
    print(num_calls)

    # Print sorted user ids
    for user_id in user_ids:
        print(user_id)