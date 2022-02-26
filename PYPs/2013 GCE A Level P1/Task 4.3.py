"""
Q4 - Task 4.3
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
        """
        while numSold < 0 or numSold > 60:
            print 'number sold is not in the range 0 to 60! Re-enter'
            numSold = input('Frenquency ... ')
        """
        sizeList.append(size)
        freqList.append(numSold)

        size = input('Next X value ...  <ZZZ to END> ')
        if numValues == 6:
            size = 'ZZZ'

    # output
    print ('\n+++++++++++++++++++++++++++++++++++++++++++++++++++')
    print ('Frequency distribution')
    print ('+++++++++++++++++++++++++++++++++++++++++++++++++++\n')

    highestFreq = max(freqList)
    if highestFreq <= 60:   # need no scaling
        for i in range(0, numValues): 
            freq = freqList[i]
            print (sizeList[i].ljust(20) + freq*'=')

    else:                   # need scaling
        if highestFreq//60 == highestFreq/60:
            scale = highestFreq // 60
        else :
            scale = highestFreq // 60 + 1

        freqDict = {}    # original freq : scaled freq
        for i in range(0, numValues):
            freq = freqList[i] // scale
            freqDict[freqList[i]] = freq
            print (sizeList[i].ljust(20) + freq*'=')  

        # print horizontal axis
        offset = 0
        freq = list(freqDict.keys())
        freq.sort()                # in ascending order
        print ()
        scaleOutput = ''
        for i in range(0, len(freqDict)):
            scaleOutput += str(freq[i]).rjust(freqDict[freq[i]] - offset)
            offset = freqDict[freq[i]]

        print ('Axis: '.ljust(20)+ '^'* max(freqDict.values()))  
        print ('Frequency: '.ljust(20) + scaleOutput)

main()
