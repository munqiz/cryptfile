import os
from Crypto.Cipher import AES
from Crypto.Util.Padding import pad
import hashlib

# Set your encryption key (password)
password = "hehe123"
key = hashlib.sha256(password.encode()).digest()

# Directory with the files you want to encrypt (modify as needed)
target_dir = "C:\\Users\\Skywalker\\Desktop\\ohno.txt"

# Encrypt all .txt files
def encrypt_file(filepath):
    with open(filepath, 'rb') as f:
        data = f.read()
    cipher = AES.new(key, AES.MODE_CBC)
    ct_bytes = cipher.encrypt(pad(data, AES.block_size))
    iv = cipher.iv
    encrypted_data = iv + ct_bytes

    enc_filepath = filepath + ".enc"
    with open(enc_filepath, 'wb') as f:
        f.write(encrypted_data)

    print(f"Encrypted: {filepath} → {enc_filepath}")

# Main loop
for root, dirs, files in os.walk(target_dir):
    for file in files:
        if file.endswith(".txt"):
            full_path = os.path.join(root, file)
            encrypt_file(full_path)
