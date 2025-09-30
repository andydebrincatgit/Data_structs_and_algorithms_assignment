
# the function simply loops through the array and if a point satisfies any of the condition then it an extreme point.
def extreme_points(array):
    is_sorted = True
    for i in range(1, len(array) - 2):
        if (array[i] > array[i - 1] and array[i] > array[i + 1]) or (array[i] < array[i - 1] and array[i] < array[i + 1]):
            print(array[i])
            is_sorted = False

    if is_sorted:
        print("SORTED\n")


A =[1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

B = [1, 2, 3, 4, 24, 6, 7, 8, 9, 10]

extreme_points(A)
extreme_points(B)

# If for all n in the range (1 , n-2) for an array of n elements, A(n) is not an extreme point then A(n-1)<A(n)<A(n+1)
# or A(n-1)>A(n)>A(n+1)
# Which by induction means the list is sorted in ascending or descending order.
