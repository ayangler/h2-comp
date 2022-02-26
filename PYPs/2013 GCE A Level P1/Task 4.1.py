"""
Q4 - Task 4.1
"""


def main():
    # initialize
    sizeList = []
    freqList = []
    numValues = 0

    # input X values and its frequency
    size = input('Next X value ...  <ZZZ to END> ')
    while numValues < 6 and size != 'ZZZ':
        numValues += 1

        numSold = int(input('Frequency ... '))
        while numSold < 0 or numSold > 60:
            print('number sold is not in the range 0 to 60! Re-enter')
            numSold = int(input('Frenquency ... '))

        sizeList.append(size)
        freqList.append(numSold)

        size = input('Next X value ...  <ZZZ to END> ')
        if numValues == 6:
            size = 'ZZZ'

    # output
    print('\n+++++++++++++++++++++++++++++++++++++++++++++++++++')
    print('Frequency distribution')
    print('+++++++++++++++++++++++++++++++++++++++++++++++++++\n')

    for i in range(0, numValues):
        print(sizeList[i].ljust(20) + freqList[i] * '|')


main()
