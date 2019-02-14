# Michael Stoffel <mstoffe2@wvup.edu> and Jeremi Swann <jswann1@wvup.edu>
# WVUP Spring 2019 MATH318 Project 5

def irand(n,m): #Generate an array of length n made up of random integers between 0 and m without replacement
    import random
    b=list(range(n))
    b=random.sample(range(m),n)
    return b

# Generate A and B

A=irand(100, 200); B=irand(100,200) # Generate A and B with 100 elements each

# Intersection of A and B

print("Intersection of A and B")
def intersection(A, B):
    intAB = [value for value in A if value in B]
    return intAB
print(intersection(A, B))

# Sort set A into ascending order
print("List A sorted into ascending order")
print(sorted(A))
# Sort set B into ascending order
print("List B sorted into ascending order")
print(sorted(B))