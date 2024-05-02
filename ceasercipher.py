def encrypt(text, shift):
    encrypted_text = ""
    for char in text:
        if char.isalpha():  # Check if character is an alphabet
            shifted = ord(char) + shift
            if char.islower():  # Check if character is lowercase
                if shifted > ord('z'):
                    shifted -= 26
            elif char.isupper():  # Check if character is uppercase
                if shifted > ord('Z'):
                    shifted -= 26
            encrypted_text += chr(shifted)
        else:
            encrypted_text += char
    return encrypted_text


def decrypt(text, shift):
    decrypted_text = ""
    for char in text:
        if char.isalpha():  # Check if character is an alphabet
            shifted = ord(char) - shift
            if char.islower():  # Check if character is lowercase
                if shifted < ord('a'):
                    shifted += 26
            elif char.isupper():  # Check if character is uppercase
                if shifted < ord('A'):
                    shifted += 26
            decrypted_text += chr(shifted)
        else:
            decrypted_text += char
    return decrypted_text


def main():
    while True:
        choice = input("Choose 'E' for encryption, 'D' for decryption, or 'Q' to quit: ").upper()
        if choice == 'Q':
            print("Exiting program.")
            break
        elif choice == 'E':
            message = input("Enter the message to encrypt: ")
            shift = int(input("Enter the shift value: "))
            encrypted_message = encrypt(message, shift)
            print("Encrypted message:", encrypted_message)
        elif choice == 'D':
            message = input("Enter the message to decrypt: ")
            shift = int(input("Enter the shift value: "))
            decrypted_message = decrypt(message, shift)
            print("Decrypted message:", decrypted_message)
        else:
            print("Invalid choice. Please enter 'E', 'D', or 'Q'.")


if __name__ == "__main__":
    main()
