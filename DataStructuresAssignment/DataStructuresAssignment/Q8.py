
import sys
# This method simply finds the root of a given number by taking f(x) as x^2 - n and then using the newton-raphson
# method to find an approximation given a starting guess.
# The method repeats for the given number of iterations and calculates the next approximation by the formula.


def newton_raphson(n, iterations, x1):
    if iterations >= 300 or n<=0:
        print("Invalid input\n")
        return 0
    x2 = 0
    for i in range(iterations):
        # A simple check to avoid division by 0
        if x1 != 0:
            x2 = x1 - ((x1**2)-n)/(2*x1)
        else:
            print("error")
            return 0
        x1 = x2
    return abs(x2)


# expected answer 1.414213562
print(newton_raphson(2, 20, -2))
print(newton_raphson(2, 20, 2))
