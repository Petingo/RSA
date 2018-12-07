import RSA

private_key, public_key = RSA.gen_key(1024)

print("private_key: " + str(private_key))
print("public_key: " + str(public_key))
print("----------")

plaintext = input("Please input plaintext: ")
print("plaintext: " + str(plaintext))
ciphertext = RSA.encrypt(plaintext, public_key)
print("ciphertext: " + str(ciphertext))
decrypt_result = RSA.decrypt(ciphertext, private_key)
print("decrypt result: ", decrypt_result)
