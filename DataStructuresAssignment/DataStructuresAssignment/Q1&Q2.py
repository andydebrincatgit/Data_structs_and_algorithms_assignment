import numpy as np
import random as rand


def swap(array, i, j):
    temp = array[i]
    array[i] = array[j]
    array[j] = temp


def shell_sort(array):
    swaps = True
    length = len(array)
    jump = length // 2
    while jump > 0 and swaps:
        swaps = False
        for i in range(0, length - jump):
            if array[i] > array[i + jump]:
                swap(array, i, i + jump)
                swaps = True
        if jump != 1:
            jump //= 2


def quicksort(array, first, last):
    if first < last:
        left = first + 1
        right = last
        pivot_index = get_pivot_index(array, first, last)
        swap(array, pivot_index, first)
        while True:
            while array[left] < array[first] and left < last:
                left += 1
            while array[right] >= array[first] and right > first:
                right -= 1
            if left < right:
                swap(array, left, right)
            if left >= right:
                break

        swap(array, first, right)
        quicksort(array, first, right - 1)
        quicksort(array, right + 1, last)


# This function is used by the quicksort to get a pivot, and it works by taking a prime number of elements
# from the array and picking their median in order to maximise the chances of a good pivot
# The median is found by first sorting, using a selection sort and then simply taking middle element
def get_pivot_index(array, first, last):
    prime = 13

    if last - first > prime:
        temp = rand.sample(range(first, last), prime)
        counter = 1
        while counter < prime:
            item_to_compare = array[temp[counter]]
            item_index = temp[counter]
            sub_counter = counter-1
            while sub_counter > 0 and array[temp[sub_counter]] > item_to_compare:
                temp[sub_counter+1] = temp[sub_counter]
                sub_counter -= 1
                temp[sub_counter+1] = item_index
            counter += 1
        pivot = temp[prime // 2]
    else:
        pivot = (last + first) // 2
    return pivot


# This algorith implements merging sorted arrays in the way the merge sort does by iterating over both simultaneously
# using two pointers and always picking the smallest. Finally, it adds the remaining elements of the other arrays
def merge_arrays(arr1, arr2):

    len_1 = len(arr1)
    len_2 = len(arr2)

    ret = np.empty((len_1 + len_2), dtype=int)
    arr1_counter = 0
    arr2_counter = 0
    counter = 0

    while arr1_counter < len_1 and arr2_counter < len_2:
        if arr1[arr1_counter] < arr2[arr2_counter]:
            ret[counter] = arr1[arr1_counter]
            arr1_counter += 1
        else:
            ret[counter] = arr2[arr2_counter]
            arr2_counter += 1
        counter += 1

    while arr1_counter < len_1:
        ret[counter] = arr1[arr1_counter]
        arr1_counter += 1
        counter += 1

    while arr2_counter < len_2:
        ret[counter] = arr2[arr2_counter]
        arr2_counter += 1
        counter += 1

    return ret


def is_sorted(array):
    flag = True
    i = 1
    while i < len(array)-2 and flag:
        if (array[i] > array[i - 1] and array[i] > array[i + 1]) or (array[i] < array[i - 1] and array[i] < array[i + 1]):
            flag = False
        i += 1
    return flag


sizeA = 256
sizeB = 200
A = np.empty(sizeA, dtype=int)
B = np.empty(sizeB, dtype=int)

for k in range(sizeA):
    A[k] = rand.randint(0, 1024)
    if k < sizeB:
        B[k] = rand.randint(0, 1024)

print("Array A :\n", A)
print("Sorted : ", is_sorted(A), "\n")
shell_sort(A)
print("Array A :\n", A)
print("Sorted : ", is_sorted(A), "\n")

print("Array B :\n", B)
print("Sorted : ", is_sorted(B), "\n")
quicksort(B, 0, len(B) - 1)
print("Array B :\n", B)
print("Sorted : ", is_sorted(B), "\n")

C = merge_arrays(A, B)
print("Array C :\n", C)
print("Sorted : ", is_sorted(C), "\n")

