import os
import base64
from cryptography.hazmat.primitives.ciphers.aead import AESGCM


def encrypt_message(message: str):
    # Generate a new 256-bit AES key
    key = AESGCM.generate_key(bit_length=256)

    # Generate a random 12-byte nonce
    nonce = os.urandom(12)

    aesgcm = AESGCM(key)

    # Encrypt the message
    ciphertext = aesgcm.encrypt(
        nonce,
        message.encode(),
        None
    )

    return key, nonce, ciphertext


def decrypt_message(key, nonce, ciphertext):
    aesgcm = AESGCM(key)

    # Decrypt the message
    plaintext = aesgcm.decrypt(
        nonce,
        ciphertext,
        None
    )

    return plaintext.decode()


if __name__ == "__main__":
    message = "This is a secure message."

    key, nonce, ciphertext = encrypt_message(message)

    print("Original Message:", message)
    print("AES-256 Key:", base64.b64encode(key).decode())
    print("Nonce:", base64.b64encode(nonce).decode())
    print("Encrypted Data:", base64.b64encode(ciphertext).decode())

    decrypted = decrypt_message(key, nonce, ciphertext)

    print("Decrypted Message:", decrypted)
