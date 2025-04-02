import os
import pytest
from cryptography.fernet import Fernet
from src.file_decryption import decrypt_file

@pytest.fixture
def setup_encrypted_file(tmp_path):
    """Create an encrypted file and key for testing"""
    # Create a key
    key = Fernet.generate_key()
    key_path = tmp_path / 'test.key'
    with open(key_path, 'wb') as key_file:
        key_file.write(key)

    # Create original file
    original_content = b'This is a test file for decryption.'
    original_file_path = tmp_path / 'test_original.txt'
    with open(original_file_path, 'wb') as f:
        f.write(original_content)

    # Encrypt the file
    f = Fernet(key)
    encrypted_content = f.encrypt(original_content)
    encrypted_file_path = tmp_path / 'test_original.txt.encrypted'
    with open(encrypted_file_path, 'wb') as f:
        f.write(encrypted_content)

    return {
        'key_path': str(key_path),
        'encrypted_file_path': str(encrypted_file_path),
        'original_content': original_content
    }

def test_successful_decryption(setup_encrypted_file):
    """Test successful file decryption"""
    decrypted_file_path = decrypt_file(
        setup_encrypted_file['encrypted_file_path'], 
        setup_encrypted_file['key_path']
    )

    # Verify decrypted file exists
    assert os.path.exists(decrypted_file_path)

    # Verify content
    with open(decrypted_file_path, 'rb') as f:
        decrypted_content = f.read()
    
    assert decrypted_content == setup_encrypted_file['original_content']

def test_nonexistent_encrypted_file(tmp_path):
    """Test decryption with non-existent encrypted file"""
    with pytest.raises(FileNotFoundError):
        decrypt_file(
            str(tmp_path / 'nonexistent.encrypted'), 
            str(tmp_path / 'test.key')
        )

def test_nonexistent_key_file(tmp_path):
    """Test decryption with non-existent key file"""
    with pytest.raises(FileNotFoundError):
        decrypt_file(
            str(tmp_path / 'test.txt.encrypted'), 
            str(tmp_path / 'nonexistent.key')
        )

def test_invalid_key(setup_encrypted_file, tmp_path):
    """Test decryption with invalid key"""
    # Generate a different key
    invalid_key = Fernet.generate_key()
    invalid_key_path = tmp_path / 'invalid.key'
    with open(invalid_key_path, 'wb') as key_file:
        key_file.write(invalid_key)

    with pytest.raises(ValueError):
        decrypt_file(
            setup_encrypted_file['encrypted_file_path'], 
            str(invalid_key_path)
        )