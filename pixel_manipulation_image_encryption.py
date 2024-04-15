from PIL import Image

def encrypt_image(image_path, key):
    try:
        img = Image.open(image_path)
        width, height = img.size
        pixels = img.load()

        for y in range(height):
            for x in range(width):
                r, g, b = pixels[x, y]
                pixels[x, y] = (r ^ key, g ^ key, b ^ key)

        encrypted_image_path = image_path.split('.')[0] + "_encrypted.png"
        img.save(encrypted_image_path)
        print("Image encrypted successfully!")
        return encrypted_image_path
    except FileNotFoundError:
        print("Error: Image file not found.")
        return None

def decrypt_image(image_path, key):
    try:
        img = Image.open(image_path)
        width, height = img.size
        pixels = img.load()

        for y in range(height):
            for x in range(width):
                r, g, b = pixels[x, y]
                pixels[x, y] = (r ^ key, g ^ key, b ^ key)

        decrypted_image_path = image_path.split('_')[0] + "_decrypted.png"
        img.save(decrypted_image_path)
        print("Image decrypted successfully!")
        return decrypted_image_path
    except FileNotFoundError:
        print("Error: Image file not found.")
        return None

def main():
    image_path = input("Enter the full path to the image file: ")
    key = int(input("Enter the encryption/decryption key (an integer): "))

    choice = input("Encrypt or Decrypt? (E/D): ").upper()

    if choice == 'E':
        encrypted_image_path = encrypt_image(image_path, key)
        if encrypted_image_path:
            print("Encrypted image saved as:", encrypted_image_path)
    elif choice == 'D':
        decrypted_image_path = decrypt_image(image_path, key)
        if decrypted_image_path:
            print("Decrypted image saved as:", decrypted_image_path)
    else:
        print("Invalid choice!")

if __name__ == "__main__":
    main()
