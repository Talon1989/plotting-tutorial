import random
from clss01.food import Food
# from lesson60021.searchTree import maxVal
# from lesson60021.searchTree import testMaxVal


def buildLargeMenu(numItems, maxVal, maxCost):
    items = []
    for i in range(numItems):
        items.append(Food('food n:'+str(),
                          random.randint(1, maxVal),
                          random.randint(1, maxCost)))
    return items


# for numItems in (5, 10, 15, 20, 25, 30, 35, 40, 45):
#     items = buildLargeMenu(numItems, 90, 250)
#     testMaxVal(items, 750, printItems=False)


def fib(n):
    if n == 0 or n == 1:
        return 1
    else:
        return fib(n-1) + fib(n-2)


# memoized implementation of fibonacci
def fast_fib(n, memo={}):
    """ assumes n is an int >= 0 , memo used only by recursive calls
        Returns Fibonacci of n"""
    if n == 0 or n == 1:
        return 1
    try:
        return memo[n]
    except KeyError:
        result = fast_fib(n-1, memo) + fast_fib(n-2, memo)
        memo[n] = result
        return result



print(fast_fib(120, {}))






























