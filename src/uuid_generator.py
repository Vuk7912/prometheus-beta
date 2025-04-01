import uuid

def generate_uuid() -> str:
    """
    Generate a Universally Unique Identifier (UUID).

    Returns:
        str: A randomly generated UUID as a string in standard format.

    Examples:
        >>> uuid_value = generate_uuid()
        >>> len(uuid_value) == 36  # Standard UUID length
        True
        >>> '-' in uuid_value  # Contains hyphens
        True
    """
    return str(uuid.uuid4())