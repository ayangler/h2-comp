"""
Task 1.2
"""
def main():
    # read data from file and store in wordList
    # wordList format:  [(term,occ)]
    
    wordList =[]
    inF = open('WORDS2.TXT','r')
    term = inF.readline().rstrip()
    while term != '':
        occ = int(inF.readline().rstrip())
        wordList.append((term, occ))   
        term = inF.readline().rstrip()
    inF.close()

    # compute the highest number of occurrrences
    maxOcc = wordList[0][1]    
    maxTerms = []
       
    for term, occ in wordList:
        if occ > maxOcc:
            maxOcc = occ
            maxTerms = [term]
        elif occ == maxOcc:
            maxTerms.append(term)

    print ('Highest occurring term(s):')
    for term in maxTerms:
           print (term)
         
main()
