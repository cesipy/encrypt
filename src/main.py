import os
from cryptography.fernet import Fernet
import argparse

from logger import Logger

logger = Logger()


def encrypt(plaintext: str, fernet: Fernet) -> bytes:
    plaintext_bytes = plaintext.encode("utf-8")
    cipher = fernet.encrypt(plaintext_bytes)

    return cipher


def decrypt(cipher, fernet: Fernet) -> str: 
    decrypted_text = fernet.decrypt(cipher)
    plain_text = decrypted_text.decode("utf-8")

    return plain_text


def generate_key() -> bytes: 
    key = Fernet.generate_key()
    logger.log(f"key: {key.decode()}, len: {len(key.decode())}")   

    return key


def encrypt_file(file_path: str, fernet: Fernet) -> None:
    with open(file_path, "r") as file: 
        plaintext = file.read()

    cipher = encrypt(plaintext, fernet)

    encrypted_file_path = file_path + ".encrypted"
    with open(encrypted_file_path, "wb") as file: 
        file.write(cipher)
    

def decrypt_file(file_path: str, fernet: Fernet) -> None:
    with open(file_path, "rb") as file: 
        cipher = file.read()
    
    decrypted_text = decrypt(cipher, fernet)

    # TODO: Function to generate name for decrypted file
    decrypted_file_path = file_path + ".decrypted"
    with open(decrypted_file_path, "w") as file: 
        file.write(decrypted_text)



def main(): 
    parser = argparse.ArgumentParser(description="Encrypt or decrypt a file.")
    group  = parser.add_mutually_exclusive_group(required=True)
    group.add_argument("--encrypt", metavar="filename", help="The name of the file to encrypt.")
    group.add_argument("--decrypt", nargs=2, metavar=("filename", "key"), help="The name of the file to decrypt and the decryption key.")
    
    args = parser.parse_args()

    if args.encrypt:
        filename = args.encrypt
        key = generate_key()
        print(f"key: {key.decode()}")
        
        f = Fernet(key)
        encrypt_file(filename, f)
    
    elif args.decrypt:
        filename, key = args.decrypt
        key = key.encode('utf-8')
        f = Fernet(key)

        decrypt_file(filename, f)



if __name__ == '__main__':
    main()
    