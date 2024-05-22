def ipvalidation(ip_address):
    # splits into bytes
    bytes = ip_address.split('.')
    
    # checks if the IP address has exactly four bytes
    if len(bytes) != 4:
        return False

    for octet in bytes:
        # Check if each octet is a number
        if not octet.isdigit():
            return False

        # Convert octet to integer and check if it's in the valid range (0-255)
        if not 0 <= int(octet) <= 255:
            return False

    # If all checks passed, the IP address is valid
    return True

# Example usage:
ip_to_test = "192.168.1.1"
print(f"The IP address {ip_to_test} is {'valid' if validate_ip(ip_to_test) else 'invalid'}.")