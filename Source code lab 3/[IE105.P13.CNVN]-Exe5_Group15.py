def generate_key(message, key):
    key = list(key)
    if len(message) == len(key):
        return key
    else:
        for i in range(len(message) - len(key)):
            key.append(key[i % len(key)])
    return "".join(key)

def encrypt(message, key):
    encrypted_text = []
    for i in range(len(message)):
        if message[i].isalpha():
            shift = (ord(message[i].upper()) + ord(key[i].upper())) % 26
            encrypted_char = chr(shift + ord('A'))
            encrypted_text.append(encrypted_char)
        else:
            encrypted_text.append(message[i])
    return "".join(encrypted_text)

def decrypt(encrypted_message, key):
    decrypted_text = []
    for i in range(len(encrypted_message)):
        if encrypted_message[i].isalpha():
            shift = (ord(encrypted_message[i].upper()) - ord(key[i].upper()) + 26) % 26
            decrypted_char = chr(shift + ord('A'))
            decrypted_text.append(decrypted_char)
        else:
            decrypted_text.append(encrypted_message[i])
    return "".join(decrypted_text)

message = "Write an application using your chosen programming language to encrypt and decrypt a message using Vigenere cipher. Test your application by a message with at least 100 words and a key of about 10-20 letters. Then verify the result with other cryptography tools"
key = "Testyourapplication"

key = generate_key(message, key)
encrypted_message = encrypt(message, key)
decrypted_message = decrypt(encrypted_message, key)

print(f"Original Message: {message}")
print(f"Encrypted Message: {encrypted_message}")
print(f"Decrypted Message: {decrypted_message}")