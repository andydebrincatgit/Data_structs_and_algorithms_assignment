
# This recursive function works by simply finding the max of A[n-1] and find_largest(A without A[n-1])
# The base case is when there is one element, and it simply returns the element since it is the largest
def find_largest(array):
    if len(array) == 1:
        return array[0]
    else:
        temp = array[len(array)-1]
        del (array[len(array) - 1])
        return max(temp, find_largest(array))


# expected answer : 23
print(find_largest([13, 2, 4, 5, 9, 23]))
