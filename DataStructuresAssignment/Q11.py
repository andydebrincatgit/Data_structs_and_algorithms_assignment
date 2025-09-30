import math


# These functions compute sine and cosine based on their Maclaurin expansion and will take the first n terms.
# However since the terms contain large factorials, a special way of computing them was needed.
# Since every term is in the form (x^n)/n! the terms were calculated by multiplying the equivalent expression :
# x/n * x/n-1 * ... * x/1.
# These would all be terms much smaller than n! making them easier to compute. Making it possible to take in a large n
# as a parameter
def cos(x, n, s):
    ret = 0
    for i in range(n):
        temp = 1
        for j in range(1, 2*i+1):
            temp *= x/j

        ret += ((-1)**i)*temp
    return round(ret, s)


def sin(x, n, s):
    ret = 0
    for i in range(n):
        temp = 1
        for j in range(1, 2 * i + 2):
            temp *= x / j

        ret += ((-1) ** i) * temp
    return round(ret, s)


number_of_terms = 1000
significant_figures = 7

# expected value : -1
print(cos(math.pi, number_of_terms, significant_figures))

# expected value : 0.707106
print(cos(math.pi/4, number_of_terms, significant_figures))

# expected value : 0
print(sin(math.pi, number_of_terms, significant_figures))

# expected value : 0.707106
print(sin(math.pi/4, number_of_terms, significant_figures))
