from clss01.food import Food
import random
import main00


def buildLargeMenu(numItems, maxVal, maxCost):
    items = []
    for i in range(numItems):
        items.append(Food('food n:'+str(),
                          random.randint(1, maxVal),
                          random.randint(1, maxCost)))
    return items


def maxVal(toConsider: list, avail):
    """ avail is a weight
        Returns a tuple of the total value of a solution to 0/1 knapsack problem
        and the items of the solution"""
    if toConsider == [] or avail == 0:
        result = (0, ())
    elif toConsider[0].getCost() > avail:
        # Explore right branch only
        result = maxVal(toConsider[1:], avail)
    else:
        nextItem = toConsider[0]
        # Explore left branch
        withVal, withToTake = maxVal(toConsider[1:], avail-nextItem.getCost())
        withVal += nextItem.getValue()
        # Explore right branch
        withoutVal, withoutToTake = maxVal(toConsider[1:], avail)
        # Choose better branch
        if withVal > withoutVal:
            result = (withVal, withToTake+(nextItem,))
        else:
            result = (withoutVal, withoutToTake)
    return result


def fastMaxVal(toConsider: list, avail, memo={}):
    """ avails is a weight
        memo supplied by recursive calls
        Returns a tuple of the total value of a solution to the 0/1 knapsack problem
        and the subjects of that solution"""
    if (len(toConsider), avail) in memo:
        result = memo[(len(toConsider), avail)]
    elif toConsider == [] or avail == 0:
        result = (0, ())
    elif toConsider[0].getCost() > avail:
        #  Explore right branch only
        result = fastMaxVal(toConsider[1:], avail, memo)
    else:
        nextItem = toConsider[0]
        #  Explore left branch
        withVal, withToTake = fastMaxVal(toConsider[1:], avail-nextItem.getCost(), memo)
        withVal += nextItem.getValue()
        #  Explore right branch
        withoutVal, withoutToTake = fastMaxVal(toConsider[1:], avail, memo)
        #  Choose the better branch
        if withVal > withoutVal:
            result = (withVal, withToTake + (nextItem,))
        else:
            result = (withoutVal, withoutToTake)
    memo[(len(toConsider), avail)] = result
    return result


def testMaxVal(foods, maxUnits, algorithm, printItems=True):
    print('Menu contains ', len(foods), ' items')
    print('Using search tree to allocate ', maxUnits, ' calories')
    val, taken = algorithm(foods, maxUnits)
    print('Total value of items taken = ', val)
    if printItems:
        for item in taken:
            print('    ', item)


# nams = ['wine', 'beer', 'pizza', 'burger', 'fries', 'cola', 'apple', 'donut', 'cake']
# vals = [89, 90, 95, 100, 90, 79, 50, 10]
# cals = [123, 154, 258, 354, 365, 150, 95, 195]
# menu = main00.buildMenu(nams, vals, cals)
# testMaxVal(menu, 750, fastMaxVal)

for numItems in (5, 10, 15, 20, 25, 30, 35, 40, 45, 2 ^ 10):
    items = buildLargeMenu(numItems, 90, 250)
    testMaxVal(items, 750, fastMaxVal, printItems=False)






































