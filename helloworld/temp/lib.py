from .models import users, contactmodel
import hashlib
import os


def hash(password):

    salt = os.urandom(32) # Remember this
    key = hashlib.pbkdf2_hmac(
        'sha256', # The hash digest algorithm for HMAC
        password.encode('utf-8'), # Convert the password to bytes
        salt, # Provide the salt
        100000, # It is recommended to use at least 100,000 iterations of SHA-256
        )
    return salt, key
    # storage = salt + key
    #
    # # Getting the values back out
    # salt_from_storage = storage[:32]  # 32 is the length of the salt
    # key_from_storage = storage[32:]
def verifyhash(password, salt, key):

    # Use the exact same setup you used to generate the key, but this time put in the password to check
    new_key = hashlib.pbkdf2_hmac(
        'sha256',
        password.encode('utf-8'), # Convert the password to bytes
        salt,
        100000
    )

    if new_key == key:
        return True
    else:
        False
# password = "Aa123456"
# store = hash(password)
# print(f"{store[1]}")
