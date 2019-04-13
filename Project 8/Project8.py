import Project5 as p5
import Project6 as p6
import Project7 as p7

a = p5.irand(100, 200)
b = p5.irand(100, 200)

print ("\nList A:\nRandom list of 100 numbers from 0 to 200: \n"+str(a))
print ("\nList B:\nRandom list of 100 numbers from 0 to 200: \n"+str(b))


a = p6.insertionSort(a)
b = p6.insertionSort(b)

print("\nSorted List A:\n"+str(a))
print("\nSorted List B:\n"+str(b))



def xor(one, two):
    result = []
    for i in range(len(one)):
        if p7.binarySearch(two, one[i]) == -1:
            result.append(one[i])
    for i in range(len(two)):
        if p7.binarySearch(one, two[i]) == -1:
            result.append(two[i])
    result = p6.insertionSort(result)
    return result

x = xor(a,b)
print ("\nxor:\n"+str(x))

def bpop(one, two):
    result = []
    for i in range(len(two)):
        if p7.binarySearch(one, two[i]) == -1:
            result.append(two[i])
    return result

bp = bpop(a, b)
print ("\nbpop:\n"+str(bp))

x.append(bp[:])

print ("\nxor append bpop:\n" + str(x))