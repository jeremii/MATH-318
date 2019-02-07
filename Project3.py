import Project2

def run(): 
    print( "P \t Q \t P^Q \t ~(P^Q)  ~P \t ~Q \t ~Pv~Q \t iff \t implies" )
    for p in (True, False):
        line = ""
        for q in (True, False):
            line += str(p) + " \t " + str(q) + " \t "
            line += str(p == q) + " \t "
            line += str(p != q) + " \t "
            line += str(not p) + " \t " + str(not q) + " \t "
            line += str(not p or not q) + " \t " 
            line += str(Project2.iff(not p, not q)) + " \t "
            line += str(Project2.implies( not p, not q))
            print line
            line = ""
run()