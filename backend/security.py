import hashlib
import os
from cryptography.fernet import Fernet

# Generate a key for encryption
def generate_key():
    key = Fernet.generate_key()
    with open('secret.key', 'wb') as key_file:
        key_file.write(key)
    return key

# Load the key from the key file
def load_key():
    return open('secret.key', 'rb').read()

# Encrypt a message
def encrypt_message(message):
    key = load_key()
    f = Fernet(key)
    encrypted_message = f.encrypt(message.encode())
    return encrypted_message

# Decrypt a message
def decrypt_message(encrypted_message):
    key = load_key()
    f = Fernet(key)
    decrypted_message = f.decrypt(encrypted_message).decode()
    return decrypted_message

# Hash a password
def hash_password(password):
    return hashlib.sha256(password.encode()).hexdigest()

# Verify a password
def verify_password(stored_password, provided_password):
    return stored_password == hash_password(provided_password)
