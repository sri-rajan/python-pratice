import time
print(time.time())
def bubble_sort(nums):
    # We set swapped to True so the loop looks runs at least once
    swapped = True
    while swapped:
        swapped = False
        for i in range(len(nums) - 1):
            if nums[i] > nums[i + 1]:
                # Swap the elements
                nums[i], nums[i + 1] = nums[i + 1], nums[i]
                # Set the flag to True so we'll loop again
                swapped = True


# Verify it works
random_list_of_nums = [5, 2, 1, 8, 4]
bubble_sort(random_list_of_nums)
print(random_list_of_nums)
print(time.time())


#another method of doing this
"""
collection=[1,6,3,4,7,3,1,9,5,1,5,4,8,99,5,34,2,1,88,4,33,1,89,53] #1,3,3,4,6,7
length = len(collection)
for i in range(length - 1):
    swapped = False
    for j in range(length - 1 - i):
        if collection[j] > collection[j + 1]:
            swapped = True
            collection[j], collection[j + 1] = collection[j + 1], collection[j]
    if not swapped:
        break  # Stop iteration if the collection is sorted.
print(collection)
"""
























