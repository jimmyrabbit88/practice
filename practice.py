import math

n = 600851475143
sq = math.sqrt(n)
sqfloor = math.floor(sq)
print (sqfloor)

for number in range(1,sqfloor):
    if n%number == 0:
        factor = n/number
        primeroot = math.floor(math.sqrt(factor))
        for number in range (3, primeroot):
            if factor%number == 0:
                prime = False
        