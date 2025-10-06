#!/usr/bin/env python3

import secrets
import string

def generate_password(length=12, use_special_chars=True):
    characters = string.ascii_letters + string.digits
    if use_special_chars:
        characters += string.punctuation

    password = ''.join(secrets.choice(characters) for _ in range(length))
    return password

# Example usage
print("Generated password:", generate_password(16))
