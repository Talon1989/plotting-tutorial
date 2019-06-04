import random


def rollDie():
    """returns a randomly chosen int between 1 and 6"""
    # return random.randint(1, 6)  # same
    return random.choice([1, 2, 3, 4, 5, 6])


# def squareRoot(x: float, epsilon: float):
#     """ Assumes x and epsilon are of type float x>=0 and epsilon > 0
#         Returns float y such that x-epsilon <= y*y <= x+epsilon"""
#     y = x/2
#     while True:
#         print(y)
#         if x-epsilon <= y**2 <= x+epsilon:
#             return y
#         else:
#             if y**2 > x+epsilon:
#                 y = y - y/2
#             else:
#                 y = y + y/2


def testRoll(n=10):
    result = ''
    for _ in range(n):
        result += str(rollDie()) + ", "
    return result[:-2]


# random.seed(123)


def runSim(goal, numTrials=1000):
    """stochastically returns probability of sequence of roll dices over numTrials tries"""
    total = 0
    for _ in range(numTrials):
        result = ''
        for _ in range(len(goal)):
            result += str(rollDie())
        if result == goal:
            total += 1
    print('estimated probability: ' + str(round(total / numTrials, 8)))
    print('actual probability: ' + str(round(1 / 6 ** len(goal), 8)))

# print(testRoll(5))


runSim('11111')


