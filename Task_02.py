import numpy as np
import PIL.Image

def encrypt_image(image_path, method):
  """Encrypts an image using a specified method.

  Args:
    image_path: The path to the image file.
    method: The encryption method to use.

  Returns:
    The encrypted image data.
  """

  image = PIL.Image.open(image_path)
  pixels = np.array(image)

  if method == "swap_pixels":
    rows, cols, _ = pixels.shape
    for i in range(0, rows, 2):
      for j in range(0, cols, 2):
        pixels[i, j], pixels[i+1, j+1] = pixels[i+1, j+1], pixels[i, j]
  elif method == "add_constant":
    pixels += 50
  elif method == "multiply_constant":
    pixels *= 0.8

  return pixels

def decrypt_image(encrypted_pixels, method):
  """Decrypts an image using a specified method.

  Args:
    encrypted_pixels: The encrypted image data.
    method: The decryption method to use.

  Returns:
    The decrypted image data.
  """

  if method == "swap_pixels":
    rows, cols, _ = encrypted_pixels.shape
    for i in range(0, rows, 2):
      for j in range(0, cols, 2):
        encrypted_pixels[i, j], encrypted_pixels[i+1, j+1] = encrypted_pixels[i+1, j+1], encrypted_pixels[i, j]
  elif method == "add_constant":
    encrypted_pixels -= 50
  elif method == "multiply_constant":
    encrypted_pixels /= 0.8

  return encrypted_pixels

def main():
  while True:
    print("Image Encryption/Decryption")
    print("1. Encrypt")
    print("2. Decrypt")
    print("3. Exit")
    choice = int(input("Enter your choice: "))

    if choice == 1:
      image_path = input("Enter the path to the image: ")
      encrypted_pixels = encrypt_image(image_path, method)
      # Save the encrypted image as a new file
      encrypted_image = PIL.Image.fromarray(encrypted_pixels)
      encrypted_image.save("encrypted_image.jpg")
      print("Image encrypted successfully.")
    elif choice == 2:
      image_path = input("Enter the path to the encrypted image: ")
      encrypted_pixels = np.array(PIL.Image.open(image_path))
      decrypted_pixels = decrypt_image(encrypted_pixels, method)
      # Save the decrypted image as a new file
      decrypted_image = PIL.Image.fromarray(decrypted_pixels)
      decrypted_image.save("decrypted_image.jpg")
      print("Image decrypted successfully.")
    elif choice == 3:
      print("Exiting...")
      break
    else:
      print("Invalid choice. Please try again.")

if __name__ == "__main__":
  main()