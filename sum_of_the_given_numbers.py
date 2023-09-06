def sumof(x,y):
    return x+y
n=int(input())
for i in range(n):
    a, b = map(int,input().split())
    print(sumof(a,b))