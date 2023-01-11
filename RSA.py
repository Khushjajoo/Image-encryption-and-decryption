
import random


#fnction for finding gcd of two numbers using euclidean algorithm
def gcd(a, b):
    while b != 0:
        a, b = b, a % b
    return a

#uses extened euclidean algorithm to get the d value
def get_d(e, z):
    ###################################your code goes here#####################################
    # function that calculates the extended euclidean algorithm
    t1 = 0
    t2 = 0
    i1 = 1
    i2 = 0
    j1 = 0
    j2 = 1
    add = z
    while e % z != 0:
        m = e % z 
        r = e // z 
        t1 = i1 - r*j1 
        t2 = i2 - r*j2
        i1 = j1
        i2 = j2
        j1 = t1
        j2 = t2
        e = z 
        z = m 
        if t1 < 0:
            while t1 < 0:
                t1 += add
    return t1
    
    
def is_prime (num):
    if num > 1: 
      
        # Iterate from 2 to n / 2  
       for i in range(2, num//2): 
         
           # If num is divisible by any number between  
           # 2 and n / 2, it is not prime  
           if (num % i) == 0: 
               return False 
               break
           else: 
               return True 
  
    else: 
        return False

def generate_keypair(p, q):
    if not (is_prime(p) and is_prime(q)):
        raise ValueError('Both numbers must be prime.')
    elif p == q:
        raise ValueError('p and q cannot be equal')
    ###################################your code goes here#####################################
    n = p*q
    z = (p-1)*(q-1)
    e = random.randint(1, n)
    while gcd(e,z) != 1:
        e = random.randint(1, n)
    return ((e, n), (get_d(e, z), n))

def encrypt(pk, plaintext):
    ###################################your code goes here#####################################
    #plaintext is a single character
    #cipher is a decimal number which is the encrypted version of plaintext
    #the pow function is much faster in calculating power compared to the ** symbol !!!
    cipher = (pow(ord(plaintext),pk[0],pk[1]))
    return cipher

def decrypt(pk, ciphertext):
    ###################################your code goes here#####################################
    #ciphertext is a single decimal number
    #the returned value is a character that is the decryption of ciphertext
    plain = chr((pow(ciphertext,pk[0],pk[1])))
    return ''.join(plain)
