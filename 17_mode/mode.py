import collections
def mode(nums):
    """Return most-common number in list.

    For this function, there will always be a single-most-common value;
    you do not need to worry about handling cases where more than one item
    occurs the same number of times.

        >>> mode([1, 2, 1])
        1

        >>> mode([2, 2, 3, 3, 2])
        2
    """

# list of elements to calculate mode
num_list = [21, 13, 19, 13, 19, 13]

# Print the list
print(num_list)

# calculate the frequency of each item
data = collections.Counter(num_list)
data_list = dict(data)

# Print the items with frequency
print(data_list)

# Find the highest frequency
max_value = max(list(data.values()))
mode_val = [num for num, freq in data_list.items() if freq == max_value]
if len(mode_val) == len(num_list):
   print("No mode in the list")
else:
   print("The Mode of the list is : " + ', '.join(map(str, mode_val)))
