import random, sys

# set recursion limit to 10000 or it will reach the init limit 1000 when running extend_gcd()
sys.setrecursionlimit(10000)

# square and multiply（快速冪）
# x ^ h mod n
def fast_pow(x, h, n):
    y = 1
    h = bin(h)[2:] # convert h into binary
    for i in range(len(h)):
        y = (y ** 2) % n
        if h[i] == '1':
            y = (y * x) % n
    return y

# 歐幾里得算法（輾轉相除法）
def gcd(a, b):
	while b != 0:
		a, b = b, a % b
	return a

# 擴展歐幾里得算法
def extend_gcd(a, b):
     if b == 0:
         return 1, 0, a
     else:
         x, y, gcd = extend_gcd(b, a % b)
         x, y = y, (x - (a // b) * y)
         return x, y, gcd

# 求 a 對同於 m 的乘法反元素
def invert(a, m):
    x, y, gcd = extend_gcd(a, m)
    if (gcd == 1):
        return x % m
    else:
        return None

# miller-rabin test，用於驗證質數
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

        b = fast_pow(a, m, n)

        if b != 1 and b != n - 1:
            i = 1
            while i < k and b != n - 1:
                b = (b ** 2) % n
                if b == 1:
                    return False
                i = i + 1

            if b != n - 1:
                return False

        confidence -= 1

    return True

# 生成大質數
def gen_big_prime(bits=1024):
    tmp = random.getrandbits(bits)
    # if the prime < 5, there will be an error when running 'random.randrange(n - 4) + 2' in miller_rabin_test() 
    while tmp < 5 or miller_rabin_test(tmp) == False:
        tmp = random.getrandbits(bits)
    return tmp

# 生成鑰匙
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

    return private_key, public_key, p, q

# 加密
def encrypt(plaintext, key):
    ciphertext = []
    for c in plaintext:
        ciphertext.append(fast_pow(ord(c), key[1], key[0]))

    return ciphertext

# 解密
def decrypt(ciphertext, key):
    plaintext = ""
    for c in ciphertext:
        plaintext += chr(fast_pow(c, key[1], key[0]))

    return plaintext

# 用中國剩餘定理加速的解密
def decrypt_with_chinese_remainder(ciphertext, private_key, p, q):
    d = private_key[1]
    d_p = d % (p-1)
    d_q = d % (q-1)
    q_inv = invert(q, p)

    plaintext = ""
    for c in ciphertext:
        m1 = fast_pow(c, d_p, p)
        m2 = fast_pow(c, d_q, q)
        h = (q_inv * (m1 - m2)) % p
        m = m2 + h * q
        plaintext += chr(m)

    return plaintext