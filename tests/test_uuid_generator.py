import re
import uuid

from src.uuid_generator import generate_uuid

def test_generate_uuid_returns_string():
    """Test that the function returns a string."""
    result = generate_uuid()
    assert isinstance(result, str), "Result should be a string"

def test_generate_uuid_format():
    """Test the UUID matches the standard UUID format."""
    result = generate_uuid()
    
    # Validate UUID format using regex
    uuid_pattern = r'^[0-9a-f]{8}-[0-9a-f]{4}-[0-9a-f]{4}-[0-9a-f]{4}-[0-9a-f]{12}$'
    assert re.match(uuid_pattern, result), "UUID does not match standard format"

def test_generate_uuid_uniqueness():
    """Test that multiple generated UUIDs are unique."""
    uuids = set(generate_uuid() for _ in range(1000))
    assert len(uuids) == 1000, "Generated UUIDs should be unique"

def test_generate_uuid_valid_uuid():
    """Test that the generated UUID can be parsed by uuid module."""
    result = generate_uuid()
    parsed_uuid = uuid.UUID(result)
    assert str(parsed_uuid) == result, "Generated UUID should be valid"

def test_generate_uuid_version():
    """Test that the generated UUID is version 4."""
    result = generate_uuid()
    parsed_uuid = uuid.UUID(result)
    assert parsed_uuid.version == 4, "UUID should be version 4"