from functools import reduce
import time
import numpy as np

# squareroots = [i**2 for i in range(1,101)]
# squareroots_reverse = squareroots[::-1]

# def binary_operation(operation, a, b):
#     return operation(a,b)

# print(binary_operation(sumar,4,5))

# print(binary_operation(
#     lambda x,y: x+y,
#     4,
#     5
# ))

# Memoize

def slow_sum(x,y):
    time.sleep(x+y)
    return x+y


def memoize(slow_function):
    cache = {} # dict
    def memoized_function(*args):
        key = '-'.join([str(arg) for arg in args])
        if key in cache:
            return cache[key]
        cache[key] = slow_function(*args)
        return cache[key]
    return memoized_function
    



def slow_factorial(n):
    time.sleep(n)
    return( reduce(
        lambda x,y: x*y,
        list(range(1,n+1)))
    )
    # y=1
    # for i in range(1,n+1):
    #     y = y*i
    # return y

cache_factorial = memoize(slow_factorial)
cache_sum = memoize(slow_sum)
print("Empieza")
for i in range(11):
    print(cache_sum(2,1))
print("Termina")
