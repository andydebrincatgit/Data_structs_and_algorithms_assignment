
# The function simply uses the trial division method up till root of n, and it increments q by 2 since all even numbers
# are not prime.
def is_prime(n):
    if n <= 1:
        return False
    prime = True
    q = 2
    while prime and q*q <= n:
        if n % q == 0:
            prime = False
        else:
            if q == 2:
                q += 1
            else:
                q += 2

    return prime


# This method was implemented using a flag array, which starts by assuming all numbers are prime, and iterates through
# the array each time marking all multiples of a number to be false.
def sieve_of_eratosthenes(n):

    primes = [True] * (n+1)
    primes[0] = False
    primes[1] = False
    ret = []

    for i in range(2, n):
        if primes[i]:
            ret.append(i)
            j = 2*i
            while j <= n:
                primes[j] = False
                j += i

    return ret


print(is_prime(4))
print(is_prime(1283))
test = sieve_of_eratosthenes(100)
print(test, len(test))
