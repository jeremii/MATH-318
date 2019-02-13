# Michael Stoffel <mstoffe2@wvup.edu> and Jeremi Swann <jswann1@wvup.edu>
def implies( p, q ): # Define Implication Function
    if p:
        return q
    else:
        return True

def iff( p, q ):    #Define if and only if
    if p == q:
        return True
    else:
        return False


def testImplies():      #Define a function to test implication
    print("TEST: IMPLIES")
    for p in (True, False):
        for q in (True, False):
            print(str(p) + " \t " + str(q) + " \t " + str(implies(p, q)))
    

def testIff():  #Define a function to test if and only if
    print("TEST: IFF")
    for p in (True, False):
        for q in (True, False):
            print( str(p) + " \t "+ str(q) + " \t " + str(iff(p, q)))

testImplies()

testIff()