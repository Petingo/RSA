import RSA

plaintext = input("Please input plaintext: ")
key_bits = input("key bits: ")

print("generating keys...")
private_key, public_key, p, q = RSA.gen_key(int(key_bits))

print("")

print("-----keys-----")
print("private_key: " + str(private_key))
print("public_key: " + str(public_key))
print("--------------")


print("")


print("----result----")
print("plaintext: " + str(plaintext))

ciphertext = RSA.encrypt(plaintext, public_key)
print("ciphertext: " + str(ciphertext))

decrypt_result = RSA.decrypt(ciphertext, private_key)
print("decrypt result (normal)  : ", decrypt_result)

decrypt_result2 = RSA.decrypt_with_chinese_remainder(ciphertext, private_key, p, q)
print("decrypt result (with CRT): ", decrypt_result)

print("--------------\n")