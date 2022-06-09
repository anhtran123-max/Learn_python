n=int(input())
x,y = [int(x) for x in input().split()]

if n%2 ==0:
    if x==1 or y==1: 
        print('White')
    elif x <= n//2 and y< n//2:
        print('White')
    elif y<= n//2 and x <n//2:
        print('White')
    elif (x == n/2 and y == n/2) or (x == (n/2) + 1 and y == n/2) or (x == (n/2) and y == (n/2) + 1):
        print("White")
    else:
        print("Black")
else: 
    if x==1 or y==1: 
        print('White')
    elif x <= (n//2) + 1 and y < n//2:
        print('White')
    elif y<= (n//2) +1 and x < n//2:
        print('White')
    elif x == (n/2)+1 and y == (n/2)+1:
        print("White")
    else:
        print("Black")