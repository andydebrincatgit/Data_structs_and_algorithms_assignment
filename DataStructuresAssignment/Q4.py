

def find_2_pairs(array):

    # first remove all duplicates taking O(n) time to reduce steps taken in the algorithm
    array = list(set(array))

    # pairs is the return list will contain all those pairs of pairs that obey the requisite rules in the question
    pairs = []

    # products will be a dictionary that maps all possible products in the given array to all the pairs that when
    # multiplied give the product.

    products = {}
    n = len(array)

    for i in range(n):

        # The second loop is only going from i+1 till n because all the products from 0 till i are symmetric with
        # those from i+1 till n and will cause repetition

        for j in range(i + 1, n):
            product = array[i] * array[j]
            # if the product is not already present in the list of products then the list of pairs that map onto it
            # is initialised
            if product not in products:
                products[product] = []
            # Then, if the pair or its symmetry are not present in the list that maps onto the product, it is added.
            # This avoids repetition
            if (array[i], array[j]) and (array[j], array[i]) not in products[product]:
                products[product].append((array[i], array[j]))

    # Finally the product dictionary is traversed, and all those products having two or more pairs mapping onto it
    # are taken in a binomial manner where if there are n pairs mapping onto a product, then there will be n choose 2
    # pairs of pairs. These pairs of pairs will then be checked to obey the rule that no number must be equal

    for product in products:
        length = len(products[product])
        if length >= 2:
            for i in range(length):
                for j in range(i + 1, length):
                    # An array is being used which stores how many different numbers in the pair of a pair there are.
                    # If this number is not 4 then some two numbers are equal rendering the pair inadequate
                    different = []
                    if products[product][i][0] not in different :
                        different.append(products[product][i][0])

                    if products[product][i][1] not in different:
                        different.append(products[product][i][1])

                    if products[product][j][0] not in different:
                        different.append(products[product][j][0])

                    if products[product][j][1] not in different:
                        different.append(products[product][j][1])

                    if len(different) == 4:
                        pairs.append((products[product][i], products[product][j]))

    return pairs


def is_valid(pairs):
    flag = True
    for pair in pairs:
        a, b = pair[0]
        c, d = pair[1]
        if a*b != c*d or (a == b) or (b == c) or (c == d) or (d == a):
            flag = False
    return flag


def has_duplicates(pairs):
    set_of_pairs = {frozenset(element for sub_tuple in pair for element in sub_tuple) for pair in pairs}
    if len(set_of_pairs) == len(pairs):
        return False
    return True


A = [1, 1, 2, 4, 6, 24, 34, 36]
pairsA = find_2_pairs(A)

for pair in pairsA:
    print(pair)

B = list(range(1, 1025))
pairsB = find_2_pairs(B)

if is_valid(pairsB) and (not has_duplicates(pairsB)):
    print("B is valid\n")

else:
    print("B is invalid\n")

