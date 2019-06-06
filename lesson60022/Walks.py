import random











class Location:
    def __init__(self, x: float, y: float):
        self.x = x
        self.y = y

    def move(self, deltaX: float, deltaY: float):
        return Location(self.x + deltaX, self.y + deltaY)

    def getX(self):
        return self.x

    def getY(self):
        return self.y

    def distFrom(self, other):
        assert isinstance(other, Location)
        xDist = self.x - other.getX()
        yDist = self.y - other.getY()
        return round(
            (xDist ** 2 + yDist ** 2) ** 0.5,
            4)

    def __str__(self):
        return '<' + str(self.x) + ' , ' + str(self.y) + '>'


class Field:
    def __init__(self):
        self.drunks = {}  # {Drunk: Location}

    def addDrunk(self, drunk, loc: Location):
        if drunk in self.drunks:
            raise ValueError('Duplicate drunk')
        else:
            self.drunks[drunk] = loc

    def getLoc(self, drunk):
        if drunk not in self.drunks:
            raise ValueError('Drunk not in the field')
        return self.drunks[drunk]

    def moveDrunk(self, drunk):
        if drunk not in self.drunks:
            raise ValueError('Drunk not in a field')
        xDist, yDist = drunk.takeStep()
        self.drunks[drunk] = self.drunks[drunk].move(xDist, yDist)


# base class to be inherited
class Drunk:
    def __init__(self, name: str):
        self.name = name

    def __str__(self):
        return 'Drunk named ' + self.name


class UsualDrunk(Drunk):
    @staticmethod
    def takeStep():
        return random.choices([(0,1), (0,-1), (1,0), (-1,0)])[0]


class ColdDrunk:
    @staticmethod
    def takeStep():
        return random.choices([(0,.9), (0,1.1), (1,0), (-1,0)])[0]


def walk(f: Field, d, numSteps: int):
    """ assumes d is a Drunk in f, numSteps >= 0
        moves d numSteps times
        Returns the distance between the final location and the location at the start of the walk"""
    start = f.getLoc(d)
    for _ in range(numSteps):
        f.moveDrunk(d)
    return start.distFrom(f.getLoc(d))


def simWalks(numSteps: int, numTrials: int, dClass: Drunk):
    """ assumes numSteps >= 0, numTrials > 0, dClass is a subClass of Drunk
        simulates numTrials walks of numSteps each
        Returns a list of the final distances for each trial"""
    distances = []
    for _ in range(numTrials):
        f = Field()
        homer = dClass
        f.addDrunk(homer, Location(0,0))
        distances.append(walk(f, homer, numSteps))
    return distances


def drunkTest(walkLengths: tuple, numTrials, dClass):
    """ assumes walkLengths a sequence of ints >= 0
        for each number of steps in walkLengths, runs simWalks and prints results"""
    for numSteps in walkLengths:
        distances = simWalks(numSteps, numTrials, dClass)
        print(dClass.__name__, ' random walk of ' + str(numSteps) + ' steps.')
        print('Mean = ' + str( round(sum(distances) / len(distances)) ))
        print('Max = ' + str(max(distances)) + ' ; Min = ' + str(min(distances)))



# random.seed(0)
drunkTest((10, 100, 1000, 10000), 100, ColdDrunk)


def simAll(drunkKinds, walkLengths, numTrials):
    for dCalss in drunkKinds:
        drunkTest(walkLengths, numTrials, dCalss)


















