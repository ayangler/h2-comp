# 2013 GCE A Level P1

"""
Task 1.1
"""


def main():
    # read data from file and store in wordList
    # wordList format:  [(term,occ)]

    wordList = []
    inF = open('WORDS1.TXT', 'r')
    term = inF.readline().rstrip()
    while term != '':
        occ = int(inF.readline().rstrip())
        wordList.append((term, occ))
        term = inF.readline().rstrip()
    inF.close()

    # compute the highest number of occurrrences
    maxTerm, maxOcc = wordList[0]  # initialise maxTerm and maxOcc with
    # the 1st word and its occurrencs
    for term, occ in wordList:
        if occ > maxOcc:
            maxOcc = occ
            maxTerm = term

    # output the term with the highest number of occurrences
    print('Highest occurring term:', maxTerm)


main()
