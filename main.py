#Some play code to see if I can improve on a "coding nightmare" that I saw online
#The goal is to enter an integer and return the same integer written out (e.g. '1'="one")

def sub1000(i):
    '''Spells out any integer 0-999'''

    #Create lookups to translate number:word depending on its place
    oneslist = ['zero','one','two','three','four','five','six','seven','eight','nine',
                'ten','eleven','twelve','thirteen','fourteen','fifteen','sixteen','seventeen','eighteen','nineteen']
    tenslist = [None, None,'twenty','thirty','forty','fifty','sixty','seventy','eighty','ninety']

    #Convert integer to a three digit number, identify hundreds place, tens place, ones place
    hundreds = i // 100
    tens = (i % 100) // 10

    #Get 0-9, or 0-19 if tens place < 2
    ones = i % 20 if tens < 2 else i % 10

    op = ''
    #Spell out the hundreds place, with option 'and' if there are also tens or ones
    if hundreds:
        op = oneslist[hundreds] + ' hundred '
        if tens or ones:
            op += 'and '

    #if tens are between 20 and 99, spell out 'xty-' format and stick to output string
    if tenslist[tens]:
        op += tenslist[tens]
        if ones:
            op += '-'

    #Add ones place to output string
    if ones or i==0:
        op += oneslist[ones]

    return op.strip()

def numwords(number):
    """Spell out any integer up to 999 decillion"""

    i = abs(int(number))

    # Remember this before we destroy i
    huns = i % 1000

    #define category list containing magnitudes that might need to be included in the spelling
    #list 'hundred' category as empty string because this function will refer to sub1000 function, which already adds 'hundred'
    catlist = ['', 'thousand', 'million', 'billion', 'trillion', 'quadrillion', 'quintillion', 'sextillion', 'septillion', 'octillion', 'nonillion', 'decillion']
    #reading right to left, use sub1000 to spell out every set of three numbers in the sequence
    #attach the appropriate magnitude (cat) to each number depending on where it is in the sequence
    #Creates list of strings formatted like [x hundred, y thousand, z million]. List order is reversed in next step.
    wordlist = list()
    for cat in catlist:
        piece = i % 1000
        i //= 1000
        if piece or (not wordlist and i==0):
            wordlist.append(sub1000(piece) + ' ' + cat)

    #Add an 'and' between the first two words if one is not already present,
    #as in 'one billion and five' instead of 'one billion five', but not
    #'one billion and one hundred and five'
    if len(wordlist) > 1 and 0<huns<100: # and not (' and ' in wordlist[0]):
        wordlist[1] += ' and ' + wordlist[0]
        wordlist = wordlist[1:]

    #print wordlist into a paragraph list in the format 'x, y, z'
    wordlist.reverse()
    op = ", ".join(wordlist)

    if number<0:
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


for i in range(100):
    print("{:>40} {:>10}  {}".format(i, numser(i), numwords(i)))

for i in [ 1967, 1993, 1999, 2000, 2001, 2019, 200020002000, 123456789, 10**9, 10**35]:
    print("{:>40} {:>10}  {}".format(i, numser(i) if i < 4000 else "", numwords(i)))