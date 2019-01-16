
#Defines the function, lex
# takes in number of declarative statements.
# and ouputs a truth table.
def lex(n):
    # r equals 2(T&F) to the power of statement count
    r=2**n
    # first line
    line = "+---"*n+"+"
    # Vertical print out
    # For every increment in r, do this
    for i in range(r):
        a="|"
        # Print first line
        print(line)
        # Horizontal print out
        # For every increment in n, do this
        for j in range(n):
            # TRANSLATE THIS TO ENGLISH
            # if r divided by 2 to the increment+1's power
            # divided by i modulus 2 is a even number, append TRUE 
            if(i//(r/2**(j+1)))%2==0:
                a=a+" T |"
                continue
            # otherwise: append FALSE
            a = a+" F |"
        # PRINT a for every increment in r
        print(a)

lex(3)
