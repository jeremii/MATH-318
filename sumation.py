sum = 0
min = 5
max = 20
for n in range(min, max+1):
    sum = sum + n**3

print sum


short = (((max*(max+1))/2)**2)-((((min-1)*min)/2)**2)
print short
print sum == short

