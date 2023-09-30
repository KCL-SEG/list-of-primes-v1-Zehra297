"""List of prime numbers generator."""
"""ENTER YOUR SOLUTION HERE!"""

def checkPrime(num):
    if num < 2:
        return False
    for i in range (2, num):
        if num % i == 0:
            return False
    return True

def primes(number_of_primes):
    list = []
    currentNum = 0
    while (len(list) < number_of_primes):
        if checkPrime(currentNum):
            list.append(currentNum)
        currentNum += 1
    return list