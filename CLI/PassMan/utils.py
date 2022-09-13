#!/usr/bin/python
import bcrypt


def hash_password(plaintext_password: str) -> str:
    enc_plaintext_password: bytes = plaintext_password.encode('utf-8')
    salt: bytes = bcrypt.gensalt()

    hashed_password: bytes = bcrypt.hashpw(enc_plaintext_password, salt)
    return hashed_password.decode('utf_8')


def verify_password(plaintext_password: str, hashed_password: str) -> bool:
    enc_plaintext_password: bytes = plaintext_password.encode('utf-8')
    enc_hashed_password: bytes = hashed_password.encode('utf-8')

    return bcrypt.checkpw(enc_plaintext_password, enc_hashed_password)
