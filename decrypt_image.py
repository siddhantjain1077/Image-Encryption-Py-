import numpy as np
import cv2
from Crypto.Cipher import AES
from Crypto.Util.Padding import unpad

KEY_FILE = "aes_key.bin"
ENCRYPTED_FILE = "encrypted_image.bin"
META_FILE = "image_meta.txt"
OUTPUT_IMAGE = "decrypted_output.jpg"

def reverse_pixel_manipulation(image):
    reversed_img = np.flip(image, axis=1)
    reversed_img = cv2.bitwise_not(reversed_img)
    return reversed_img

def decrypt_image():
    with open(KEY_FILE, 'rb') as kf:
        key = kf.read()
    with open(ENCRYPTED_FILE, 'rb') as ef:
        iv = ef.read(16)
        ciphertext = ef.read()
    with open(META_FILE, 'r') as mf:
        h, w, c = map(int, mf.read().split(','))

    cipher = AES.new(key, AES.MODE_CBC, iv)
    plaintext = unpad(cipher.decrypt(ciphertext), AES.block_size)

    image_array = np.frombuffer(plaintext, dtype=np.uint8)
    image_array = image_array.reshape((h, w, c))

    original_image = reverse_pixel_manipulation(image_array)
    cv2.imwrite(OUTPUT_IMAGE, original_image)

    print("[+] Image decrypted and saved to:", OUTPUT_IMAGE)

if __name__ == "__main__":
    decrypt_image()
