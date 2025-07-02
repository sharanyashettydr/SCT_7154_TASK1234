def caesar_cipher(text, shift, mode='encrypt'):
    result = ""
    
    if mode == 'decrypt':
        shift = -shift

    for char in text:
        if char.isalpha():
            start = ord('A') if char.isupper() else ord('a')
            result += chr((ord(char) - start + shift) % 26 + start)
        else:
            result += char

    return result

def main():
    print("=== Caesar Cipher ===")
    mode = input("Do you want to (E)ncrypt or (D)ecrypt? ").lower()
    if mode not in ['e', 'd']:
        print("Invalid choice.")
        return

    message = input("Enter your message: ")
    try:
        shift = int(input("Enter shift value (e.g., 3): "))
    except ValueError:
        print("Shift must be an integer.")
        return

    if mode == 'e':
        encrypted = caesar_cipher(message, shift, mode='encrypt')
        print("Encrypted message:", encrypted)
    else:
        decrypted = caesar_cipher(message, shift, mode='decrypt')
        print("Decrypted message:", decrypted)

if __name__ == "__main__":
    main()