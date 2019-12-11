#Some play code to see if I can improve on a "coding nightmare" that I saw online
#The goal is to enter an integer and return the same integer written out (e.g. '1'="one")

def sub1000(i):
    '''Spells out any integer 0-999'''
    #Create dictionaries to translate number:word depending on its place
    onesdict = dict({1:'one',2:'two',3:'three',4:'four',5:'five',6:'six',7:'seven',8:'eight',9:'nine'})
    tensdict = dict({2:'twenty',3:'thirty',4:'forty',5:'fifty',6:'sixty',7:'seventy',8:'eighty',9:'ninety'})
    teensdict = dict({0:'ten',1:'eleven',2:'twelve',3:'thirteen',4:'fourteen',5:'fifteen',6:'sixteen',7:'seventeen',8:'eighteen',9:'nineteen'})
    #Convert integer to a three digit number, identify hundreds place, tens place, ones place
    s = str(i).zfill(3)
    hundreds = int(s[0])
    tens = int(s[1])
    ones = int(s[2])
    #Check if the hundreds>0 and if tens+ones>0, spell out 'X hundred and' format
    if hundreds>0:
        if (tens+ones)>0:
            a = 'and '
        else:
            a = ''
        op = str(onesdict[hundreds]) + ' hundred ' + a
    else:
        op = ''
    #if tens are between 20 and 99, spell out 'xty-y' format and stick to output string
    if 2<=tens:
        if ones>0:
            h = '-' + str(onesdict[ones])
        else:
            h = ''
        op+= str(tensdict[tens]) + h
    #if tens+ones are 10-19, use the teen dictionary for irregular cases
    elif tens==1:
        op+= str(teensdict[ones])
    #only reach this point if tens=0, determine ones spelling and stick to output string
    elif ones>0:
        op+= str(onesdict[ones])
    return op.strip()

def numwords(i):
    """Spell out any integer up to 999 decillion"""
    if i==0:
        return 'zero'
    #define category list containing magnitudes that might need to be included in the spelling
    #list 'hundred' category as empty string because this function will refer to sub1000 function, which already adds 'hundred'
    catdict = ['', 'thousand', 'million', 'billion', 'trillion', 'quadrillion', 'quintillion', 'sextillion', 'septillion', 'octillion', 'nonillion', 'decillion']
    #reading right to left, use sub1000 to spell out every set of three numbers in the sequence
    #attach the appropriate magnitude (cat) to each number depending on where it is in the sequence
    #Creates list of strings formatted like [x hundred, y thousand, z million]. List order is reversed in next step.
    s = str(abs(i))
    cat = 0
    wordlist = list()
    while s!='':
        if int(s[-3:])!=0:
            wordlist.append(sub1000(int(s[-3:])) +' ' + catdict[cat])
        cat+=1
        s = s[:-3]
    #print wordlist into a paragraph list in the format 'x, y, z'
    #if hundreds space is 1-99, add an 'and' as in 'one billion and five' instead of 'one billion, one hundred and five'
    wordlist.reverse()
    for x in wordlist:
        ix = wordlist.index(x)
        huns = int(str(abs(i))[-3:])
        #start output string with first element
        if ix==0:
            op=x
        #for the last element for numbers between 1-99, add 'and x'
        elif ix==(len(wordlist)-1) and 0<huns<100:
            op+=' and '+x
        #for all other elements, add ', x'
        else:
            op+=', '+x
    if i<0:
        op = 'negative '+op
    return op.strip()

def numser(i):
    """Convert any integer up to 3,999 to roman numerals"""
    onesdict = {'i':'I','v':'V','x':'X'}
    tensdict = {'i':'X','v':'L','x':'C'}
    hundict = {'i':'C','v':'D','x':'M'}
    mildict = {'i':'M','v':'','x':''}
    alldict = [mildict, hundict,tensdict,onesdict]
    translist = ['i','ii','iii','iv','v','vi','vii','viii','ix']
    if i>3999:
        return "Failure: Please enter a number between 1 and 3,999"
    s = str(abs(i)).zfill(4)
    n = list()
    for x in range(4):
        n.append(int(s[x]))
    op = ''
    for x in range(4):
        if n[x]!=0:
            d = alldict[x]
            st = translist[n[x]-1]
            st = st.replace('i',d['i'])
            st = st.replace('v',d['v'])
            st = st.replace('x',d['x'])
            op+=st
    return op


for i in [ 1967, 1993, 1999, 2000, 2001, 2019]:
    print("{} {:>10}  {}".format(i, numser(i), numwords(i)))