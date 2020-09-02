'''
Please readme.md before coming here

'''

# importing stuff
from math import floor
from matplotlib import pyplot as plt
from lel import names


def tupperFormula(x, y, fixedWidth, fixedHeight):
    # 1/2 < floor(mod(floor(y/17)*2^(-17*floor(x)-mod(floor(y),17)),2))
    # 1/2 < floor( floor(y / 17) * 2^(-17*floor(x)-mod(floor(y),17)) % 2)

    a = y//fixedHeight
    b = fixedHeight*x + y % fixedHeight
    c = 2**b
    d = a // c
    e = (d) % 2
    return 0.5 < e


def getCoordinateLists(fixedWidth, fixedHeight, k):

    xList = []
    yList = []
    for x in range(fixedWidth):
        for y in range(fixedHeight):

            if tupperFormula(x, y+k, fixedWidth, fixedHeight):
                # plt.bar(x, bottom=y, height=1,
                #         width=1, linewidth=0, color='black')
                xList.append(x)
                yList.append(y)
    return (xList, yList)


def getLabelsForYTicks(yticks):
    tempList = ['K']
    for i in yticks[1::]:
        tempList.append(f'K + {i}')
    return tempList


def implementAndSave(k, filename):

    # constants
    fixedWidth = 106
    fixedHeight = 17

    #  setup stuff ig
    plt.rc('patch', antialiased=False)
    plt.title('tupper')

    # getting coordinates ready
    xList, yList = getCoordinateLists(fixedWidth, fixedHeight, k)

    # plotting
    plt.scatter(xList, yList, marker='s')
    print('done')

    # asthetics etc.
    plt.rc('font', size=10)

    plt.axis('scaled')

    # -- getting the ticks right
    plt.xticks(range(0, fixedWidth, 20))
    yticks = list(range(0, fixedHeight, 5))
    plt.yticks(yticks, getLabelsForYTicks(yticks))

    # inverting axes
    plt.gca().invert_yaxis()
    plt.gca().invert_xaxis()

    # saving to file
    plt.savefig(f'./imgs/{filename}')
    # plt.show() // in case you want to show it as well


# implementAndSave(names['originalTupper'], 'balle.png')
