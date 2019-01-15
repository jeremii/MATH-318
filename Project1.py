def lex(n):
    r=2**n
    line = "+---"*n+"+"
    for i in range(r):
        a="|"
        print(line)
        for j in range(n):
            if(i//(r/2**(j+1)))%2==0:
                a=a+" T |"
                continue
            a = a+" F |"
        print(a)

lex(3)
