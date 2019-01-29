def implies( p, q ):
    if p:
        return q
    else:
        return True

def iff( p, q ):
    if p == q:
        return True
    else:
        return False


def testImplies():
    print("TEST: IMPLIES")
    for p in (True, False):
        for q in (True, False):
            print(str(p) + " \t " + str(q) + " \t " + str(implies(p, q)))
    

def testIff():
    print("TEST: IFF")
    for p in (True, False):
        for q in (True, False):
            print( str(p) + " \t "+ str(q) + " \t " + str(iff(p, q)))

testImplies()
testIff()
