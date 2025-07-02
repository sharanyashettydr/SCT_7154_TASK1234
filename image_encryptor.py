from PIL import Image
import os

def apply_math(value, operation, op_value):
    if operation == "add":
        return (value + op_value) % 256
    elif operation == "subtract":
        return (value - op_value) % 256
    elif operation == "xor":
        return value ^ op_value
    else:
        return value

def encrypt_image(input_path, output_path, method, operation=None, op_value=0):
    if not os.path.exists(input_path):
        print("❌ Input image not found:", input_path)
        return

    img = Image.open(input_path)
    pixels = img.load()
    width, height = img.size

    for x in range(width):
        for y in range(height):
            r, g, b = pixels[x, y]

            if method == "swap":
                new_r, new_g, new_b = b, g, r

            elif method == "math":
                new_g = apply_math(g, operation, op_value)
                new_r, new_b = r, b
                new_r, new_g, new_b = new_r, new_g, new_b

            else:
                print("❌ Invalid method.")
                return

            pixels[x, y] = (new_r, new_g, new_b)

    img.save(output_path)
    print("✅ Image encrypted and saved to", output_path)

def decrypt_image(input_path, output_path, method, operation=None, op_value=0):
    if not os.path.exists(input_path):
        print("❌ Input image not found:", input_path)
        return

    img = Image.open(input_path)
    pixels = img.load()
    width, height = img.size

    for x in range(width):
        for y in range(height):
            r, g, b = pixels[x, y]

            if method == "swap":
                original_r, original_g, original_b = b, g, r

            elif method == "math":
                if operation == "add":
                    original_g = apply_math(g, "subtract", op_value)
                elif operation == "subtract":
                    original_g = apply_math(g, "add", op_value)
                elif operation == "xor":
                    original_g = apply_math(g, "xor", op_value)
                else:
                    original_g = g
                original_r, original_b = r, b

                original_r, original_g, original_b = original_r, original_g, original_b

            else:
                print("❌ Invalid method.")
                return

            pixels[x, y] = (original_r, original_g, original_b)

    img.save(output_path)
    print("✅ Image decrypted and saved to", output_path)

def main():
    print("\n=== 🔐 Image Encryption Tool ===")
    mode = input("👉 Choose mode - Encrypt or Decrypt (e/d): ").strip().lower()

    if mode not in ['e', 'd']:
        print("❌ Invalid mode selected.")
        return

    method = input("👉 Choose method - Swap or Math (swap/math): ").strip().lower()

    if method not in ['swap', 'math']:
        print("❌ Invalid method selected.")
        return

    operation = None
    op_value = 0

    if method == "math":
        print("📌 Available operations: add, subtract, xor")
        operation = input("👉 Choose operation: ").strip().lower()

        if operation not in ['add', 'subtract', 'xor']:
            print("❌ Invalid operation.")
            return

        try:
            op_value = int(input("👉 Enter value (0-255): "))
            if not (0 <= op_value <= 255):
                raise ValueError
        except ValueError:
            print("❌ Please enter a valid number between 0 and 255.")
            return

    input_path = input("📥 Enter input image path (e.g., test.jpg): ").strip()
    output_path = input("📤 Enter output image path (e.g., result.jpg): ").strip()

    if mode == 'e':
        encrypt_image(input_path, output_path, method, operation, op_value)
    else:
        decrypt_image(input_path, output_path, method, operation, op_value)

if __name__ == "__main__":
    main()