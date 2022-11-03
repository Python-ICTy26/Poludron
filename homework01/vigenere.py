def encrypt_vigenere(plaintext: str, keyword: str) -> str:
    """
    Encrypts plaintext using a Vigenere cipher.

    >>> encrypt_vigenere("PYTHON", "A")
    'PYTHON'
    >>> encrypt_vigenere("python", "a")
    'python'
    >>> encrypt_vigenere("ATTACKATDAWN", "LEMON")
    'LXFOPVEFRNHR'
    """
    ciphertext = ""
    key = ""
    while len(key) < len(plaintext):
        key += keyword
    key = key[: len(plaintext)]
    for i in range(len(plaintext)):
        if plaintext[i].isalpha():
            if plaintext[i].isupper():
                shift = ord(key[i % len(key)]) - ord("A")
                ciphertext += chr(((ord(plaintext[i]) - ord("A")) + shift) % 26 + ord("A"))
            else:
                shift = ord(key[i % len(key)]) - ord("a")
                ciphertext += chr(((ord(plaintext[i]) - ord("a")) + shift) % 26 + ord("a"))
        else:
            ciphertext += plaintext[i]
    return ciphertext


def decrypt_vigenere(ciphertext: str, keyword: str) -> str:
    """
    Decrypts a ciphertext using a Vigenere cipher.

    >>> decrypt_vigenere("PYTHON", "A")
    'PYTHON'
    >>> decrypt_vigenere("python", "a")
    'python'
    >>> decrypt_vigenere("LXFOPVEFRNHR", "LEMON")
    'ATTACKATDAWN'
    """
    plaintext = ""
    key = ""
    while len(key) < len(ciphertext):
        key += keyword
    key = key[: len(ciphertext)]
    for i in range(len(ciphertext)):
        if ciphertext[i].isalpha():
            if ciphertext[i].isupper():
                shift = ord(key[i % len(key)]) - ord("A")
                plaintext += chr(((ord(ciphertext[i]) - ord("A")) - shift) % 26 + ord("A"))
            else:
                shift = ord(key[i % len(key)]) - ord("a")
                plaintext += chr(((ord(ciphertext[i]) - ord("a")) - shift) % 26 + ord("a"))
        else:
            plaintext += ciphertext[i]
    return plaintext
