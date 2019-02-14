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

# Union of A and B

#Print label for Union of A and B
print("Union of A and B")
#Define function for union of A and B
def Union(A, B):
    # Set variable for union of A and B to list A + list B and then sort them into ascending order
    unionAB = sorted(A + B)
    # Remove Duplicate values from list that is Union of A and B
    removeDupUnionAB = list( dict.fromkeys(unionAB))
    return removeDupUnionAB
#Print Union of A and B
print(Union(A, B))

# Print List A sorted into ascending order again
# Label List A
print("List A sorted into ascending order")
print(sorted(A))
# Print List B sorted into ascending order again
# Label List B
print("List B sorted into ascending order")
print(sorted(B))

#Print not A in ascending order
#Print label for not A in ascending order
print("Not A in ascending order")

# Make a list of all possible numbers from 0 - 200
allNumbers = list(range(201))
# Define function to find the difference of list A and the list of all possible numbers from 0-200 (allNumbers - A)
def missingFromA(allNumbers, A):
    # Set variable for difference of allNumbers and A to list allNumbers - A and then sort them into ascending order
    # Find the difference between list allNumbers and list A
    notInA = [i for i in allNumbers + A if i not in allNumbers or i not in A]
    return sorted(notInA)

notA = missingFromA(allNumbers, A)

print(notA)

#Print A-B in ascending order
#Print label for A-B in ascending order
print("A-B in ascending order")
#Define function for A-B
def diff(A, B):
    # Set variable for difference of A and B to list A - list B and then sort them into ascending order
    #Find the difference between list A and list B
    diffAB = [i for i in A + B if i not in A or i not in B]
    return sorted(diffAB)

print(diff(A, B))
