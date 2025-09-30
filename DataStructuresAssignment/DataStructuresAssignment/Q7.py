import csv


# This is a very simple algorithm to implement the collatz sequence, by simply dividing by 2 if even or multiplying by
# 3n and adding 1 if odd.
def collatz(n):
    ret = [n]
    temp = n
    while temp != 1:
        if temp % 2 == 0:
            temp //= 2
        else:
            temp = 3 * temp + 1
        ret.append(temp)
    return ret


# The collatz sequences of the numbers from 2-512 are then stored in a list which is then written to a csv file

collatz_list = []
for i in range(2, 513):
    collatz_list.append(collatz(i))

filename = "Collatz_sequences.csv"

with open(filename, 'w') as csvfile:
    pointer = csv.writer(csvfile)
    pointer.writerows(collatz_list)