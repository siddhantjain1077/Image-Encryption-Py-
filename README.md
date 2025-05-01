# 🔐 Image Encryption using Pixel Manipulation and AES

A mini project that encrypts and decrypts image files using a combination of simple pixel manipulation and strong AES-256 encryption in CBC mode. Built with Python, OpenCV, and PyCryptodome.

---

## 🧠 Overview

This project demonstrates how to:
- Securely encrypt an image using **AES encryption** (Advanced Encryption Standard).
- Add an extra layer of security with **pixel manipulation** (e.g., inverting and flipping).
- Decrypt and reconstruct the image back to its original form.

---

## 📁 Project Structure

flowchart TD
    A["Start"] --> B["Load Original Image\ncv2.imread()"]
    B --> C["Pixel Manipulation\n- Invert colors\n- Flip horizontally"]
    C --> D["Convert to Byte Stream\n.tobytes()"]
    D --> E["Pad to AES Block Size\npad(..., AES.block_size)"]
    E --> F["Encrypt with AES-256 CBC\nGenerate key & IV\ncipher.encrypt()"]
    F --> G["Save Encrypted File\n(iv + ciphertext)"]
    G --> H["Save AES Key\naes_key.bin"]
    G --> I["Save Metadata\nimage_meta.txt"]
    I --> J["End Encryption"]

    subgraph Decryption
      J --> K["Load Encrypted File, Key & Metadata"]
      K --> L["Separate IV & Ciphertext"]
      L --> M["Decrypt with AES-256 CBC\ncipher.decrypt + unpad"]
      M --> N["Convert Bytes to Array\nnp.frombuffer → reshape"]
      N --> O["Reverse Pixel Manipulation\n- Flip horizontally\n- Invert colors"]
      O --> P["Save Decrypted Image\ncv2.imwrite()"]
      P --> Q["End"]
    end
