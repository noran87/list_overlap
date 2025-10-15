
import random

#randomly generate twp lists
a = [random.randint(1,90) for _ in range(10)]
b = [random.randint(1, 20) for _ in range(12)]

#find common elements between the two lists
output = list(set([x for x in a if x in b]))

#print the output
print('the first random list: ', a)
print('the second random list: ', b)
print(output)
