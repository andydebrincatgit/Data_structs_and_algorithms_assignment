
# This function simply calculates the fibonacci numbers from 1 to n and adds them to the total.
# If n<1 then 0 is returned
def sum_fibonacci(n):
    if n == 1:
        return 1
    if n == 2:
        return 2
    if n < 1:
        return 0

    total = 2
    x_n_1 = 1
    x_n_2 = 1

    for i in range(3, n+1):
        temp = x_n_1 + x_n_2
        x_n_2 = x_n_1
        x_n_1 = temp
        total += temp
    return total


# expected answer: 33
print(sum_fibonacci(7))
# expected answer: 0
print(sum_fibonacci(-2))
# expected answer: 4
print(sum_fibonacci(3))
