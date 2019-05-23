import pylab as plt


def retire(monthly, rate, terms):
    savings = [0]
    base = [0]
    mRate = rate / 12
    for i in range(terms):
        base += [i]
        savings += [savings[-1] * (1 + mRate) + monthly]
    return base, savings


def displayRetireWMonthlies(monthlies, rate, terms):
    plt.figure('retireMonth')
    plt.clf()
    for m in monthlies:
        xvals, yvals = retire(m, rate, terms)
        plt.plot(xvals, yvals, label='retire: ' + str(m))
        plt.legend(loc='upper left')
    plt.show()


def displayRetireWRates(month, rates, terms):
    plt.figure('retireRate')
    plt.clf()
    for r in rates:
        xvals, yvals = retire(month, r, terms)
        plt.plot(xvals, yvals, label='retire: ' + str(month) + ": " + str(int(r * 100)) + '%')
        plt.legend(loc='upper left')
    plt.show()


def displayRetireWMonthliesAndRates(monthlies, rates, terms):
    plt.figure('retireMonthAndRate')
    plt.clf()
    plt.xlim(30 * 12, terms)
    mLabels = ['r', 'b', 'g', 'k']
    rLabels = ['-', 'o', '--']
    for m in monthlies:
        for r in rates:
            xvals, yvals = retire(m, r, terms)
            plt.plot(xvals, yvals,
                     mLabels[monthlies.index(m) % len(mLabels)]
                     + rLabels[rates.index(r) % len(rLabels)],
                     label='retire: ' + str(m) + ": " + str(int(r * 100)) + '%')
            plt.legend(loc='upper left')
    plt.show()


# displayRetireWMonthlies([500, 600, 700, 800, 900, 1000, 1100],
#                         .05,
#                         40*12)
#
# displayRetireWRates(800,
#                     [.03, .05, .07],
#                     40*12)

displayRetireWMonthliesAndRates([500, 700, 900, 1100],
                                [.03, .05, .07],
                                40 * 12)
