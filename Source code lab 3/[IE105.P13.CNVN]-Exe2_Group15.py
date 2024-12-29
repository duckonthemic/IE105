def caesar_cipher(text, key, mode='encrypt'):
    result = ''
    for char in text:
        if char.isalpha():
            shift = key if mode == 'encrypt' else -key
            new_char = chr((ord(char.upper()) - 65 + shift) % 26 + 65)
            result += new_char if char.isupper() else new_char.lower()
        else:
            result += char
    return result

def brute_force_caesar(ciphertext):
    print("Brute-forcing all possible keys:\n")
    for key in range(26):
        print(f"Key {key}: {caesar_cipher(ciphertext, key, mode='decrypt')}")

def main():
    print("Caesar Cipher Application")
    print("1. Encrypt a message")
    print("2. Decrypt a message")
    print("3. Brute-force a ciphertext")
    choice = input("Choose an option (1/2/3): ")

    if choice == '1':
        plaintext = input("Enter the plaintext: ")
        key = int(input("Enter the key (0-25): "))
        ciphertext = caesar_cipher(plaintext, key, mode='encrypt')
        print(f"Ciphertext: {ciphertext}")

    elif choice == '2':
        ciphertext = input("Enter the ciphertext: ")
        key = int(input("Enter the key (0-25): "))
        plaintext = caesar_cipher(ciphertext, key, mode='decrypt')
        print(f"Plaintext: {plaintext}")

    elif choice == '3':
        ciphertext = input("Enter the ciphertext: ")
        brute_force_caesar(ciphertext)

    else:
        print("Invalid choice. Please try again.")

if __name__ == "__main__":
    main()
