def encrypt_text(rawtext, a, b, c):
    asciivalue = []
    for char in rawtext:
        lettervalue = ord(char)
        if lettervalue > 127:
            raise ValueError(f"Invalid character: '{char}' — only ASCII allowed")
        asciivalue.append(float(lettervalue))
    encryptedascii = [a * x**2 + b * x + c for x in asciivalue]
    return encryptedascii
