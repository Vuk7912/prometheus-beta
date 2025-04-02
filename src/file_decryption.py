from cryptography.fernet import Fernet
import os

def decrypt_file(encrypted_file_path, key_path):
    """
    Decrypt an encrypted file using a Fernet symmetric encryption key.

    Args:
        encrypted_file_path (str): Path to the encrypted file
        key_path (str): Path to the encryption key file

    Returns:
        str: Path to the decrypted file

    Raises:
        FileNotFoundError: If encrypted file or key file does not exist
        ValueError: If key is invalid or decryption fails
    """
    # Validate input file paths
    if not os.path.exists(encrypted_file_path):
        raise FileNotFoundError(f"Encrypted file not found: {encrypted_file_path}")
    
    if not os.path.exists(key_path):
        raise FileNotFoundError(f"Key file not found: {key_path}")

    try:
        # Read the encryption key
        with open(key_path, 'rb') as key_file:
            key = key_file.read()

        # Create Fernet instance
        f = Fernet(key)

        # Read encrypted file
        with open(encrypted_file_path, 'rb') as encrypted_file:
            encrypted_data = encrypted_file.read()

        # Decrypt the file
        decrypted_data = f.decrypt(encrypted_data)

        # Create decrypted file path
        decrypted_file_path = encrypted_file_path.replace('.encrypted', '')

        # Write decrypted data to new file
        with open(decrypted_file_path, 'wb') as decrypted_file:
            decrypted_file.write(decrypted_data)

        return decrypted_file_path

    except Exception as e:
        raise ValueError(f"Decryption failed: {str(e)}")