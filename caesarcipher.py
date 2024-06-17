print("Caesar Cipher Program")

while True:
    choice = input("Do you want to encrypt or decrypt? (e/d): ").lower()
    if choice in ['e', 'd']:
        break
    print("Invalid choice! Please enter 'e' for encryption or 'd' for decryption.")

text = input("Enter your message: ")
shift = int(input("Enter shift value: "))

def caesar_cipher(text, shift, mode):
    result = ""
    for char in text:
        if char.isalpha():
            ascii_offset = 65 if char.isupper() else 97
            if mode == 'encrypt':
                result += chr((ord(char) - ascii_offset + shift) % 26 + ascii_offset)
            elif mode == 'decrypt':
                result += chr((ord(char) - ascii_offset - shift) % 26 + ascii_offset)
        else:
            result += char
    return result

if choice == 'e':
    result = caesar_cipher(text, shift, 'encrypt')
    print("Encrypted Text:", {result})
else:
    result = caesar_cipher(text, shift, 'decrypt')
    print("Decrypted Text:", {result})