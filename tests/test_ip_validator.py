import pytest
from src.ip_validator import validate_ip_address

def test_valid_ip_addresses():
    """Test various valid IP addresses"""
    valid_cases = [
        "1.2.3.4",
        "0.0.0.0",
        "9.9.9.9",
        "7.6.5.4"
    ]
    for ip in valid_cases:
        assert validate_ip_address(ip) is True, f"Failed for valid IP: {ip}"

def test_invalid_ip_addresses():
    """Test various invalid IP addresses"""
    invalid_cases = [
        # Too long parts
        "10.2.3.4",
        "1.20.3.4",
        
        # Non-digit parts
        "a.b.c.d",
        "1.2.3.x",
        
        # Incorrect number of parts
        "1.2.3",
        "1.2.3.4.5",
        
        # Empty parts
        ".1.2.3",
        "1.2.3.",
        "",
        
        # Non-string input
        123,
        None,
        [1, 2, 3, 4]
    ]
    for ip in invalid_cases:
        assert validate_ip_address(ip) is False, f"Failed for invalid IP: {ip}"

def test_edge_cases():
    """Test edge cases for IP address validation"""
    # Additional specifics checking exact behavior
    assert validate_ip_address("0.0.0.0") is True
    assert validate_ip_address("9.9.9.9") is True
    assert validate_ip_address("1.1.1.1") is True