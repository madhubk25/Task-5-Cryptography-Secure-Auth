import bcrypt


def hash_password(password: str) -> bytes:
    # Generate a unique salt and hash the password
    salt = bcrypt.gensalt(rounds=12)
    hashed_password = bcrypt.hashpw(
        password.encode(),
        salt
    )

    return hashed_password


def verify_password(password: str, hashed_password: bytes) -> bool:
    return bcrypt.checkpw(
        password.encode(),
        hashed_password
    )


if __name__ == "__main__":
    password = "TrainingPassword123!"

    hashed = hash_password(password)

    print("Password hashed successfully.")
    print("Hashed password:", hashed.decode())

    if verify_password(password, hashed):
        print("Correct password: verification successful.")

    if not verify_password("WrongPassword", hashed):
        print("Wrong password: verification failed.")
