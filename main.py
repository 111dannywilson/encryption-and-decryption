from string import ascii_lowercase, digits


def encrypt_data(text: str) -> str:
    """
    Receives a text or number and encrypts it into some form of hidden code
    Args:
        text: The normal text or word you want to encrypt
    Returns: The encrypted word of the normal text or numbers provided
    """
    encrypted_text = ""
    for i in str(text).lower():
        encrypting = encryption_bp.find(i)
        encrypted_text += encryption_bp[encrypting + 1] if i != encryption_bp[-1] else encryption_bp[0]
    return encrypted_text


def decrypt_data(encrypted_text: str) -> str:
    """
    Decrypts encrypted texts to their meaning
    Args:
        encrypted_text: Encrypted text
    Returns: Decrypted  encrypted text provided
    """
    decrypted_text = ""
    for i in str(encrypted_text).lower():
        decrypting = encryption_bp.find(i)
        decrypted_text += encryption_bp[decrypting - 1] if i != encryption_bp[0] else " "
    return decrypted_text


encryption_bp = ascii_lowercase + digits

encrypt = encrypt_data("cat")
decrypt = decrypt_data("dbu")
