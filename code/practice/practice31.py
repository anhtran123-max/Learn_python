import math
n = int(input())
sum=3 * (math.floor((n-1)/3)  *  (math.floor((n-1)/3)+1))/2 + 5 * (math.floor((n-1)/5)  *  (math.floor((n-1)/5)+1))/2-15 * (math.floor((n-1)/15) * (math.floor((n-1)/15)+1))/2 

print(sum)
