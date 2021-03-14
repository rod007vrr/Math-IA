import math

def binaryExpansion(a,b,n):
    sumAll = 0
    
    def nCk(p,q):
        return math.factorial(p)/(math.factorial(q)*math.factorial(p-q))

    for k in range(n+1):
        sumAll +=  nCk(n,k)*(a**(n-k))*(b**k)
    
    return sumAll

print(binaryExpansion(2,3,10))