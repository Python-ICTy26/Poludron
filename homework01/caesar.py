import typing as tp


def encrypt_caesar(plaintext: str, shift: int = 3) -> str:
    ciphertext = ""
    for i in plaintext:
        if i.isalpha():
            if i.isupper():
                ciphertext += chr(((ord(i) - ord("A")) + shift) % 26 + ord("A"))
            else:
                ciphertext += chr(((ord(i) - ord("a")) + shift) % 26 + ord("a"))
        else:
            ciphertext += i
    return ciphertext


def decrypt_caesar(ciphertext: str, shift: int = 3) -> str:
    plaintext = ""
    for i in ciphertext:
        if i.isalpha():
            if i.isupper():
                plaintext += chr(((ord(i) - ord("A")) - shift) % 26 + ord("A"))
            else:
                plaintext += chr(((ord(i) - ord("a")) - shift) % 26 + ord("a"))
        else:
            plaintext += i
    return plaintext

print(decrypt_caesar("SBWKRQ"))

'''def caesar_breaker_brute_force(ciphertext: str, dictionary: tp.Set[str]) -> int:
    """
    Brute force breaking a Caesar cipher.
    """
    best_shift = 0
    # PUT YOUR CODE HERE
    return best_shift'''


'''for i in plaintext:
        if i.isalpha():
            stayInAlphabet = ord(i) + shift 
            if stayInAlphabet > ord('z'):
                stayInAlphabet -= 26
            finalLetter = chr(stayInAlphabet)
            ciphertext += finalLetter
        else:
            plaintext += i'''