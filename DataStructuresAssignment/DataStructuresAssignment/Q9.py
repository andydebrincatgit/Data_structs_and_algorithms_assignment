def find_duplicates(array):
    # a flag array is used to indicate which elements have already been found by adding them to it once
    flag = []
    ret = []
    for i in range(len(array)):
        # use a search to check whether the duplicate is in the flag-list
        if array[i] in flag:
            # if it is then check if it is in the return list of duplicates
            if array[i] not in ret:
                # if it is not, then add it, resulting in a list of unique numbers that have been repeated in the array
                ret.append(array[i])
        else:
            # if the item is not in the flag list then add it to indicate that it has already been found once
            flag.append(array[i])
    return ret


# expected answer : 1,2,8
arr = [1, 1, 2, 2, 2, 3, 4, 5, 6, 7, 8, 8, 9, 10]
print(find_duplicates(arr))
