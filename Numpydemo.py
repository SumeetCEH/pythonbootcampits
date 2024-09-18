import numpy as np
#creating array using numpy
arr = np.array([0,1,2,3,5,9,11,23,4,7])
print(arr)

#print the type of numpy array
print(type(arr))

print(arr.max())
print(arr.min())
print(arr.mean())
print(arr.sum())
print(arr.std())

# print("before sorting",arr)
# arr.sort()
# print("after sorting",arr)

# Function to sort an array in descending order
def sort_descending(arr):
    arr.sort(reverse=True)
    return arr

array = [5, 2, 9, 1, 5, 6]
sorted_array = sort_descending(array)
print(sorted_array)
