import cv2
import numpy as np
from Crypto.Cipher import AES
from Crypto.Random import get_random_bytes
from Crypto.Util.Padding import pad

KEY_FILE = "aes_key.bin"
ENCRYPTED_FILE = "encrypted_image.bin"
IMAGE_PATH = "original_image.jpg"

def pixel_manipulation(image):
    manipulated = cv2.bitwise_not(image)
    manipulated = np.flip(manipulated, axis=1)
    return manipulated

def encrypt_image(image_path):
    image = cv2.imread(image_path)
    manipulated = pixel_manipulation(image)
    height, width, channels = manipulated.shape

    byte_data = manipulated.tobytes()

    key = get_random_bytes(32)  # AES-256
    cipher = AES.new(key, AES.MODE_CBC)
    ct_bytes = cipher.encrypt(pad(byte_data, AES.block_size))
    iv = cipher.iv

    # Save encrypted data
    with open(ENCRYPTED_FILE, 'wb') as f:
        f.write(iv + ct_bytes)

    # Save key + metadata
    with open(KEY_FILE, 'wb') as kf:
        kf.write(key)
    with open("image_meta.txt", 'w') as mf:
        mf.write(f"{height},{width},{channels}")

    print("[+] Image encrypted successfully.")
    print(f"[+] Encrypted file: {ENCRYPTED_FILE}")
    print(f"[+] Key saved to: {KEY_FILE}")
    print(f"[+] Metadata saved to: image_meta.txt")

if __name__ == "__main__":
    encrypt_image(IMAGE_PATH)
