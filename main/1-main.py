import pylab as plt


def example1(mySamples, myLinear, myQuadratic, myCubic, myExponential):

    plt.plot(mySamples, myLinear)
    plt.plot(mySamples, myQuadratic)
    plt.plot(mySamples, myCubic)
    plt.plot(mySamples, myExponential)
    plt.show()


def example2(mySamples, myLinear, myQuadratic, myCubic, myExponential):

    plt.figure('lin')
    plt.plot(mySamples, myLinear)
    plt.figure('quad')
    plt.plot(mySamples, myQuadratic)
    plt.figure('cube')
    plt.plot(mySamples, myCubic)
    plt.figure('expo')
    plt.plot(mySamples, myExponential)
    plt.show()


def example3(mySamples, myLinear, myQuadratic, myCubic, myExponential):

    plt.figure('lin')
    plt.clf()
    plt.title('Linear')
    plt.xlabel('sample points')
    plt.ylabel('linear function')
    plt.plot(mySamples, myLinear)

    plt.figure('quad')
    plt.clf()
    plt.title('Quadratic')
    plt.xlabel('sample points')
    plt.ylabel('quadratic function')
    plt.plot(mySamples, myQuadratic)

    plt.figure('cube')
    plt.clf()
    plt.title('Cubic')
    plt.xlabel('sample points')
    plt.ylabel('cubic function')
    plt.plot(mySamples, myCubic)

    plt.figure('expo')
    plt.clf()
    plt.title('Exponential')
    plt.xlabel('sample points')
    plt.ylabel('exponential function')
    plt.plot(mySamples, myExponential)
    plt.show()


def example4(mySamples, myLinear, myQuadratic, myCubic, myExponential):

    plt.figure('lin quad')
    plt.clf()
    plt.ylim(0, 1000)
    plt.title('Linear and Quadratic')
    plt.xlabel('sample points')
    plt.plot(mySamples, myLinear, label='linear')
    plt.plot(mySamples, myQuadratic, label='quadratic')
    plt.legend(loc='upper left')

    plt.figure('cube expo')
    plt.clf()
    plt.title('Cubic and Exponential')
    plt.xlabel('sample points')
    plt.plot(mySamples, myCubic, label='cubic')
    plt.plot(mySamples, myExponential, label='exponential')
    plt.legend(loc='upper right')

    plt.show()


def example5(mySamples, myLinear, myQuadratic, myCubic, myExponential):

    plt.figure('lin quad')
    plt.clf()
    plt.title('Linear and Quadratic')
    plt.xlabel('sample points')
    plt.subplot(211)  # n of rows, n of cols inside a plot, n of locations to use
    plt.plot(mySamples, myLinear, 'b-', label='linear', linewidth=.5)
    plt.legend(loc='upper left')
    plt.subplot(212)
    plt.plot(mySamples, myQuadratic, 'ro', label='quadratic', linewidth=3.0)
    plt.legend(loc='upper left')

    plt.figure('cube expo')
    plt.clf()
    plt.title('Cubic and Exponential')
    plt.xlabel('sample points')
    plt.yscale('log')
    plt.subplot(121)
    plt.plot(mySamples, myCubic, 'g^', label='cubic', linewidth=4.0)
    plt.yscale('log')
    plt.legend(loc='upper right')
    plt.subplot(122)
    plt.plot(mySamples, myExponential, 'r--', label='exponential', linewidth=5.0)
    plt.yscale('log')
    plt.legend(loc='upper right')

    plt.show()


my_samples = []
my_linear = []
my_quadratic = []
my_cubic = []
my_exponential = []

for i in range(0, 30):
    my_samples.append(i)
    my_linear.append(i)
    my_quadratic.append(i**2)
    my_cubic.append(i**3)
    my_exponential.append(1.5**i)


example5(my_samples, my_linear, my_quadratic, my_cubic, my_exponential)

