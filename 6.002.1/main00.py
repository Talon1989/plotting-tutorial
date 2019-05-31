from clss01.food import Food




def buildMenu(names: list, values, calories):
    """ name, values, calories lists of same length.
        name a list of strings
        values and calories lists of numbers
        returns list of Foods"""
    menu = []
    for i in range(len(values)):
        menu.append(Food(names[i], values[i], calories[i]))
    return menu


def greedy(items, maxCost, keyFunction):
    """ Assumes items a list, maxCost >= 0,
        keyFunction maps elements of items to numbers"""
    itemsCopy = sorted(items, key=keyFunction, reverse=True)
    result = []
    totalValue, totalCost = 0.0, 0.0
    for i in range(len(itemsCopy)):
        if (totalCost+itemsCopy[i].getCost()) <= maxCost:
            result.append(itemsCopy[i])
            totalCost += itemsCopy[i].getCost()
            totalValue += itemsCopy[i].getValue()
    return result, totalValue


def testGreedy(items, constraint, keyFunction):
    taken, val = greedy(items, constraint, keyFunction)
    print('Total value of items taken = ', val)
    for item in taken:
        print(' ', item)
    print('\n')


def testGreedys(foods: list, maxUnits):
    print('Use greedy by value to allocate', maxUnits, 'calories')
    testGreedy(foods, maxUnits, Food.getValue)
    print('Use greedy by cost to allocate', maxUnits, 'calories')
    testGreedy(foods, maxUnits, lambda x: 1/Food.getCost(x))
    print('Use greedy by density to allocate', maxUnits, 'calories')
    testGreedy(foods, maxUnits, Food.getDensity)


nams = ['wine', 'beer', 'pizza', 'burger', 'fries', 'cola', 'apple', 'donut', 'cake']
vals = [89, 90, 95, 100, 90, 79, 50, 10]
cals = [123, 154, 258, 354, 365, 150, 95, 195]
testGreedys(
    buildMenu(nams, vals, cals), 1000
)

