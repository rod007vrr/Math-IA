import math

def checkPrime(num):
    for x in range(2, num):
        if num%x == 0:
            return False
    else:
        return True

def findPublicKey(totient):
    
    #identify totient factors
    """ temp_totient = totient
    
    totient_factors = []
    for n in range(2, math.floor(totient/2)+1):
        while temp_totient % n == 0:
            totient_factors.append(n)
            temp_totient /= n """
    
    #loop through possible public keys
    """ for i in range(3, int(totient)):
        temp_factors = []
        #factorize item
        for q in range(2, math.floor(totient/2)+1):
            while temp_totient % q == 0:
                temp_factors.append(q)
                temp_totient /= q
        #check coprime
        if not common_member(totient_factors, temp_factors):
            return i 
        
        def common_member(a, b): 
        a_set = set(a) 
        b_set = set(b) 
        if (a_set & b_set): 
            return True 
        else: 
            return False     
            
        """
    for n in range(3, totient):
        if math.gcd(totient, n) == 1:
            return n
        
    
               

def findPrivateKey(temp_public_key, mod):
    found = False
    temp_private_key = 1
    while not found:
    
        if ((temp_public_key*temp_private_key) % mod == 1 
            and temp_private_key != temp_public_key):  
            found = True
            return temp_private_key
        else:
            temp_private_key+=1

def getImaginaryTotient(num):
    totient = ((num.real+1)*(num.imag+1))-1
    return totient

def encryption(temp_message, temp_public_key, temp_modulus):
    number_to_mod = temp_message**temp_public_key
    encrypted_message = imaginary_modulus(number_to_mod, temp_modulus)
    return encrypted_message

def decryption(temp_encrypted_message, temp_private_key, temp_modulus):
    number_to_mod = temp_encrypted_message**temp_private_key
    decrypted_message = imaginary_modulus(number_to_mod, temp_modulus)
    return decrypted_message
    
def imaginary_modulus(number, modulus):
    #do initial division
    quotient = number/modulus
    #round and shit
    quotient = round(quotient.real) + round(quotient.imag)*1j
    #execute r = a-qb
    remainder = number - (quotient*modulus)
    return remainder

    
#prime 1 definition
p = 3+2j
print(f"p: {p}")

#prime 2 definition
q = 2+1j
print(f"q: {q}")

#product of both primes
n = p*q
print(f"n: {n}\n")

#totient of P
totient_P = 5
#totient_P = int(getImaginaryTotient(p).real)
print(f"tot(p): {totient_P}")

#totient of Q
totient_Q = 3
#totient_Q = int(getImaginaryTotient(q).real)
print(f"tot(q): {totient_Q}")

#totient of product of P and Q
totient_N = (totient_P*totient_Q)
print(f"tot(n): {totient_N}\n")

#obtaining public key (e)
public_key = findPublicKey(totient_N.real)
print(f"public key: {public_key}")

#obtaining private key (d)
private_key = findPrivateKey(public_key, totient_N)
print(f"private key: {private_key}\n")

#message
message = 13
print(f"message: {message}")

encrypted_message = encryption(message, public_key, n)
print(f"encrypted message: {encrypted_message}")

decrypted_message = decryption(encrypted_message, private_key, n)
print(f"decrypted message: {decrypted_message}")