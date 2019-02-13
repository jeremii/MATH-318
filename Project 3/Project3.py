# Michael Stoffel <mstoffe2@wvup.edu> and Jeremi Swann <jswann1@wvup.edu>

import Project2

def run(): 
    print( "P \t Q \t P^Q \t ~(P^Q)  ~P \t ~Q \t ~Pv~Q \t iff" )
    for p in (True, False):
        line = ""
        for q in (True, False):
            PaQ = p == q == True
            nPaQ = PaQ == False
            nPoQ = not p or not q
            line += str(p) + " \t " + str(q) + " \t "
            line += str(PaQ) + " \t "
            line += str(nPaQ) + " \t "
            line += str(not p) + " \t " + str(not q) + " \t "
            line += str(nPoQ) + " \t " 
            line += str(Project2.iff(nPaQ, nPoQ))
            print(line)
            line = ""
run()