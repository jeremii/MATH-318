
#Defines the function, lex
# takes in number of declarative statements.
# and ouputs a truth table.
def lex(n):
    # n = count of statements
    # r = all possible combinations of T&F**n power
    # Vertical height of table
    # r equals 2(T&F) to the power of statement count
    r=2**n
    # divider line
    line = "+---"*n+"+"
    # Vertical print out
    # For every increment in r, do this
    for i in range(r):
        a = "|"
        # Print divider line
        print(line)
        # Horizontal print out
        # For every increment in n, do this
        for j in range(n):
            # if row total divided by 2 to the increment's power
            # divided by row increment is even, append TRUE 
            if(i//(r/2**(j+1)))%2==0:
                a=a+" T |"
                continue
            # otherwise: append FALSE
            a = a+" F |"
        # PRINT a for every increment in r
        print(a)
    print(line)

lex(3)
