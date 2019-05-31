from clss01.food import Food
import main00


def maxVal(toConsider: list, avail):
    """ avail is a weight
        returns a tuple of the total value of a solution to 0/1 knapsack problem
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


def testMaxVal(foods, maxUnits, printItems=True):
    print('Using search tree to allocate ', maxUnits, ' calories')
    val, taken = maxVal(foods, maxUnits)
    print('Total value of items taken = ', val)
    if printItems:
        for item in taken:
            print('    ', item)


nams = ['wine', 'beer', 'pizza', 'burger', 'fries', 'cola', 'apple', 'donut', 'cake']
vals = [89, 90, 95, 100, 90, 79, 50, 10]
cals = [123, 154, 258, 354, 365, 150, 95, 195]

menu = main00.buildMenu(nams, vals, cals)
testMaxVal(menu, 750)




































