# Task 5 - Cryptography, Key Management & Secure Authentication

## Overview

This project demonstrates basic secure cryptographic techniques as part of a cybersecurity internship practical task.

The project covers:

- AES-256-GCM symmetric encryption
- RSA-2048 digital signatures
- bcrypt password hashing
- HMAC integrity verification
- Secure key and secret storage
- Key rotation practices

## Project Files

### aes_gcm.py
Demonstrates AES-256-GCM encryption and decryption using a randomly generated nonce.

### rsa_signature.py
Demonstrates RSA-2048 key generation, digital signature creation, and signature verification using SHA-256.

### password_hashing.py
Demonstrates secure password hashing and verification using bcrypt with a salt and work factor.

### SECURITY.md
Documents secure key management, secret storage, password security, HMAC usage, and key rotation.

## Technologies Used

- Python
- AES-256-GCM
- RSA-2048
- SHA-256
- bcrypt
- HMAC
- Python Cryptography Library

## Installation

Install the required Python packages:

```bash
pip install cryptography bcrypt

Running the Programs

AES encryption:

python aes_gcm.py

RSA digital signature:

python rsa_signature.py

Password hashing:

python password_hashing.py
Security Practices

The project follows these security practices:

AES uses a 256-bit key.
A random nonce is generated for encryption.
RSA uses a 2048-bit key.
RSA signatures use SHA-256 with PSS padding.
Passwords are hashed using bcrypt.
Sensitive keys and secrets should not be stored in source code.
Private keys must not be uploaded to GitHub.
Cryptographic keys should be rotated according to security requirements.
Internship Scope

This repository is created for cybersecurity internship training and educational purposes. The examples are intended for authorized laboratory and learning environments.

Author

Madhu B.K.
