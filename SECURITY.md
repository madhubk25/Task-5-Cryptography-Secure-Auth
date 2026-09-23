# Security Documentation

## 1. AES-256-GCM Key Management

AES-256-GCM is used for authenticated encryption.

- A 256-bit AES key is generated using a secure cryptographic random generator.
- A unique 12-byte nonce is generated for each encryption operation.
- The same nonce must never be reused with the same AES key.
- Authentication provided by GCM helps detect unauthorized modification of encrypted data.
- Encryption keys should be stored in a secure secret-management system rather than directly in source code.

## 2. RSA-2048 Key Management

RSA-2048 is used for digital signatures.

- The private key must remain confidential.
- The public key can be distributed for signature verification.
- Private keys should be protected using appropriate access controls and secure key storage.
- Private keys must never be committed to GitHub.
- Keys should be rotated according to organizational security requirements.

## 3. Password Security

Passwords are protected using bcrypt.

- A unique salt is generated for each password.
- A configurable work factor is used to make password cracking more expensive.
- Plain-text passwords should never be stored.
- Password verification is performed against the stored bcrypt hash.

## 4. HMAC Integrity Protection

HMAC with SHA-256 can be used to verify message integrity and authenticity when a shared secret key is available.

- HMAC keys should be generated using a cryptographically secure random generator.
- HMAC secrets must be kept confidential.
- Verification should use constant-time comparison where appropriate.

## 5. Secret Storage

Sensitive information such as:

- Encryption keys
- Private RSA keys
- HMAC secrets
- API keys
- Database passwords

should not be stored directly in source code or committed to GitHub.

For production systems, secrets should be stored using a secure secret-management solution with appropriate access controls.

## 6. Key Rotation

A basic key-rotation process should include:

1. Generate a new cryptographic key.
2. Store the new key securely.
3. Update the application to use the new key.
4. Retain old keys only when required to decrypt existing data.
5. Remove or securely retire old keys when they are no longer required.
6. Record the rotation event for auditing.

## 7. GitHub Security

The repository should not contain:

- Private keys
- API tokens
- Real passwords
- Production encryption keys
- `.env` files containing secrets

Only demonstration code and non-sensitive training data should be uploaded.
