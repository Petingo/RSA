import random

def gcd(a, b):
	while b != 0:
		a, b = b, a % b
	return a

def extend_gcd(a, b):
     if b == 0:
         return 1, 0, a
     else:
         x, y, q = extend_gcd(b, a % b)
         x, y = y, (x - (a // b) * y)
         return x, y, q

def invert(a, m):
    x, y, gcd = extend_gcd(a, m)
    if (gcd == 1):
        return x % m
    else:
        return None

def miller_rabin_test(n, confidence=40):
    k = 0
    m = (n - 1)
    while m % 2 == 0:
        m = m // 2
        k = k + 1
    while confidence > 0:
        # choose only odd a
        a = random.randrange(n - 4) + 2
        while a % 2 == 0:
            a = random.randrange(n - 4) + 2

        b = pow(a, m, n)

        if b != 1 and b != n - 1:
            i = 1
            while i < k and b != n - 1:
                b = pow(b, 2, n)
                if b == 1:
                    return False
                i = i + 1

            if b != n - 1:
                return False

        confidence -= 1

    return True


def gen_big_prime(bits=1024):
    tmp = random.getrandbits(bits)
    while tmp < 5 or miller_rabin_test(tmp) == False:
        tmp = random.getrandbits(bits)
    return tmp

def gen_key(bits=1024):
    p = gen_big_prime(bits)
    q = gen_big_prime(bits)
    N = p * q
    phi = (p - 1) * (q - 1)

    d = None
    while d is None:

        e = random.randrange(phi)
        while gcd(e, phi) != 1:
            e = random.randrange(phi)

        d = invert(e, phi)

    private_key = N, d
    public_key = N, e

    return private_key, public_key


def encrypt(plaintext, public_key):
    ciphertext = []
    for c in plaintext:
        ciphertext.append(pow(ord(c), public_key[1], public_key[0]))

    return ciphertext

def decrypt(ciphertext, private_key):
    plaintext = ""
    for val in ciphertext:
        plaintext += chr(pow(val, private_key[1], private_key[0]))

    return plaintext

# plaintext = "2018"
# p = 71
# q = 83
# N = p * q
# phi = (p - 1) * (q - 1)

# # 隨機挑 d
# d = None
# while d is None:

#     e = random.randrange(phi)
#     while gcd(e, phi) != 1:
#         e = random.randrange(phi)

#     d = invert(e, phi)

# private_key = N, d
# public_key = N, e

# print("private_key: " + str(private_key))
# print("public_key: " + str(public_key))

# ciphertext = encrypt(plaintext, public_key)
# print("ciphertext: " + str(ciphertext))

# decrypt_result = decrypt(ciphertext, private_key)
# print("decrypt result: " + str(decrypt_result))
