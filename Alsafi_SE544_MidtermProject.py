#HAMAD REDHA ALSAFI

import random

#length of random numbers 
max_num_length = 1000000


# calculates the gcd of two numbers
def gcd(a, b):
    if b == 0:
        return a
    else:
        return gcd(b, a % b)


# calculates the modular inverse from e and t 
def egcd(b, n):
    (x0, x1, y0, y1) = (1, 0, 0, 1)
    while n != 0:
        (q, b, n) = (b // n, n, b % n)
        (x0, x1) = (x1, x0 - q * x1)
        (y0, y1) = (y1, y0 - q * y1)
    return (b, x0, y0)


# generate random prime number rather than input from user
def generate_Random_number_prim():
    while True:
        prime = True
        num = random.randint(0, max_num_length)
        if num == 2:
            return num
        if num < 2 or num % 2 == 0:
            prime = False
        else:
            for n in range(3, int(num ** 0.5) + 2, 2):
                if num % n == 0:
                    prime = False
        if prime:
            return num


def generate_key():
    p = generate_Random_number_prim()
    q = generate_Random_number_prim()
    n = p * q
  # print("n ", n)
    #pi 
    t = (p - 1) * (q - 1)
    
    # select e
    while True:
        #to return an integer number
        e = random.randint(1, t)
        g = gcd(e, t)
        if g == 1:
            break
    # aply modular inverse of e and t'''
    d = egcd(e, t)
    d = d[1]
    # make  d  positive
    d = d % t
    if (d < 0):
        d += t
    return ((e, n), (d, n))


# decrypted based on private key
def decrypt(ctext, private_key):
    #to handle any error 
    try:
        key, n = private_key
        text = ""
        for char in ctext:
            text += chr(pow(char, key, n))
        return text

    except TypeError as e:
        print(e)


# encrypt text based on puplic key
def encrypt(text, public_key):
    key, n = public_key
    ctext = []
    for char in text:
        ctext.append(pow(ord(char), key, n))
    return ctext


def encrypt_decrypt(file):
    public_key, private_key = generate_key()
   # print("Public: ", public_key)
   # print("Private: ", private_key)

    # read text file read line by line
    with open(file,"r") as f:
        lines = f.readlines()
    encrypted_lines = [] # list include output encrypted 
    # encrypt each line adding key from privous code
    for line in lines:
        encrypted_lines.append(encrypt(line, public_key))
    # write encrypted lines to encrypted.txt
    with open("encrypted.txt","w") as f:
        #write each line
        for cline in encrypted_lines:
            f.write(str(cline))
    f.close()
    # decrypt encrypted_lines and write in decrypt.txt
    with open("decrypt.txt","w") as f:
        for cline in encrypted_lines:
            f.write(decrypt(cline, private_key))
    f.close()

file = "example.txt"
encrypt_decrypt(file)

print("Open example file to read plaintext")
print("Open encrypt file to see encrypted message")
print("Open decrypt file to see decrypted message")
print("------------Thank You------------------")

