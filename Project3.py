import Project2

def run(a): 
    for p in range(True, False):
        for q in range(True, False):
            print( p + " " + q + " " )
            print ( (p == q) + " " )
            print( (p != q) + " " )
            print( (not p) + " " + (not q) + " " )
            print( (not p or not q) + " " )
            print( Project2.iff(p, q) )


run(True)