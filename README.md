# File Encryption/Decryption Script

This script provides functionalities to encrypt and decrypt files using the Fernet symmetric encryption method from the `cryptography` library. It can generate encryption keys, encrypt files with generated or provided keys, and decrypt files using provided keys.

## Features

- **Encryption**: Encrypt a file and generate a new encryption key.
- **Encryption with a provided key**: Encrypt a file using a specified encryption key.
- **Decryption**: Decrypt an encrypted file using a specified decryption key.

## Prerequisites

- `cryptography` library

Install the `cryptography` library using pip:

```bash
pip install cryptography
```

## Usage

### Encrypting a File

To encrypt a file and generate a new encryption key:

```bash
python script.py --encrypt filename
```

This will output the encryption key to the console. Make sure to save this key as it is required for decryption.

### Encrypting a File with a Provided Key

To encrypt a file using a specified encryption key:

```bash
python script.py --encrypt-with-key filename key
```

Replace `filename` with the path to your file and `key` with your encryption key.

### Decrypting a File

To decrypt an encrypted file using a specified decryption key:

```bash
python script.py --decrypt filename key
```

Replace `filename` with the path to your encrypted file and `key` with your decryption key.

## Script Details

### Functions

- `encrypt(plaintext: str, fernet: Fernet) -> bytes`: Encrypts the provided plaintext using the specified Fernet object.
- `decrypt(cipher, fernet: Fernet) -> str`: Decrypts the provided ciphertext using the specified Fernet object.
- `generate_key() -> bytes`: Generates a new Fernet key and logs it.
- `encrypt_file(file_path: str, fernet: Fernet) -> None`: Encrypts the contents of the specified file.
- `decrypt_file(file_path: str, fernet: Fernet) -> None`: Decrypts the contents of the specified file.
- `generate_file_path(file_path: str)`: Generates a new file path for the decrypted file.

### Logger

The script uses a custom `Logger` class for logging. Ensure you have a `logger.py` file with the `Logger` class implemented.

### Main Function

The `main` function parses command-line arguments to determine the operation mode (encrypt, encrypt with key, or decrypt) and calls the appropriate functions.

### Command-Line Arguments

- `--encrypt filename`: Encrypts the specified file and generates a new encryption key.
- `--encrypt-with-key filename key`: Encrypts the specified file using the provided encryption key.
- `--decrypt filename key`: Decrypts the specified file using the provided decryption key.

## Example

To encrypt a file named `example.txt` and generate a new encryption key:

```bash
python script.py --encrypt example.txt
```

To encrypt a file named `example.txt` using a specific key `my_secret_key`:

```bash
python script.py --encrypt-with-key example.txt my_secret_key
```

To decrypt a file named `example.txt.encrypted` using a specific key `my_secret_key`:

```bash
python script.py --decrypt example.txt.encrypted my_secret_key
```

## Notes

- Make sure to save your encryption keys securely, as they are essential for decrypting your files.
- The script appends `.encrypted` to the filename for encrypted files and `.decrypted` for decrypted files.

