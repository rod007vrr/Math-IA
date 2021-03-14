from decimal import Decimal
import math

def complexDivide(dividend, divisor):
    def divide(dividend, divisor):
        realQuotient = dividend.real//divisor
        realRemainder = dividend.real%divisor
        imagQuotient = dividend.imag//divisor
        imagRemainder = dividend.imag%divisor
        #return f"{dividend}/{divisor} = ({realQuotient} + {imagQuotient}i)*{divisor} + ({realRemainder} + {imagRemainder}i"
        return realRemainder + imagRemainder*1j #! MIGHT BE NEGATIVE SIGN 
    divisorToBe = ((divisor.real)**2)+((divisor.imag)**2)
    dividendToBe = (dividend*divisor.real) - ((dividend*divisor.imag)*1j) 
    return divide(dividendToBe, divisorToBe)

def gcd(a,b): 
    if b==0: 
        return a 
    else: 
        return gcd(b,a%b) 

def binaryExpansion(a,b,n):
    sumAll = Decimal(0)
    sumAll = 0
    def nCk(p,q):
        return math.factorial(p)/(math.factorial(q)*math.factorial(p-q))

    for k in range(n+1):
        sumAll +=  nCk(n,k)*(a**(n-k))*(b**k)
    
    return sumAll

p =9+4j
q = 5+4j
Message = 12
n = p*q
t = ((9*4)-1)*((5*4)-1)

for e in range(2,t): 
    if gcd(e,t)== 1: 
        break

print(e)
  
for i in range(1,10): 
    x = 1 + i*t 
    if x % e == 0: 
        d = int(x/e) 
        break
    
print(d)

lol = d

d = 222 
e = 3

ctt = Decimal(0)
ctt = pow(Message, e)
ct = complexDivide(ctt, n)

print(ct)

dtt = Decimal(0)
dtt = binaryExpansion(ct.real,ct.imag,d)
dt = complexDivide(ct, n) #this is a full prime number being divided here not just the real component, this may be part of the issue

print(dt)