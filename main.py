from art import *

def caesar_cipher(text, shift, direction):
    """
    Encrypts or decrypts a message using the Caesar cipher.

    Args:
        text (str): The input message.
        shift (int): The shift amount (positive or negative).
        direction (str): 'encode' to encrypt or 'decode' to decrypt.

    Returns:
        str: The resulting encrypted or decrypted message.
    """
    all_characters = (
        "abcdefghijklmnopqrstuvwxyz"
        "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
        "0123456789"
        " !\"#$%&'()*+,-./:;<=>?@[\\]^_`{|}~"
    )
    result = ""

    for char in text:
        if char in all_characters:
            index = all_characters.index(char)
            if direction == "encode":
                new_index = (index + shift) % len(all_characters)
            else:
                new_index = (index - shift) % len(all_characters)
            result += all_characters[new_index]
        else:
            result += char

    return result

def atbash_cipher(text):
    """
    Applies the Atbash cipher (substitution cipher).

    Args:
        text (str): The input message.

    Returns:
        str: The resulting encrypted or decrypted message.
    """
    alphabet = "abcdefghijklmnopqrstuvwxyz"
    reversed_alphabet = alphabet[::-1]
    result = ""

    for char in text:
        if char.isalpha():
            char_lower = char.lower()
            index = alphabet.index(char_lower)
            new_char = reversed_alphabet[index]
            result += new_char.upper() if char.isupper() else new_char
        else:
            result += char

    return result

def reverse_cipher(text):
    """
    Reverses the input message.

    Args:
        text (str): The input message.

    Returns:
        str: The resulting reversed message.
    """
    return text[::-1]

def main():
    print("Welcome to the Cipher Enhancer!")
    print("Choose an algorithm:")
    print("1. Caesar Cipher")
    print("2. Atbash Cipher")
    print("3. Reverse Cipher")
    print("4. Exit")

    choice = input("Enter the number of your choice: ")

    if choice == "1":
        print(logo1)
        direction = input("Type 'encode' to encrypt or 'decode' to decrypt: ").lower()
        message = input("Type your message: ")
        shift_amount = int(input("Type the shift number: "))
        encrypted_message = caesar_cipher(message, shift_amount, direction)
        print(f"Here's the {direction}d result: {encrypted_message}")
    elif choice == "2":
        print(logo2)
        message = input("Type your message: ")
        encrypted_message = atbash_cipher(message)
        print(f"Here's the Atbash result: {encrypted_message}")
    elif choice == "3":
        print(logo3)
        message = input("Type your message: ")
        reversed_message = reverse_cipher(message)
        print(f"Here's the reversed result: {reversed_message}")
    elif choice == "4":
        print("Thank you for using the Cipher Enhancer!")
    else:
        print("Invalid choice. Please select a valid option.")

if __name__ == "__main__":
    main()
