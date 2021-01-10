def rotate(text, key):
    res = ""
    for c in text:
        if c.isalpha():
            rc = ord(c) + key
            if c.isupper():
                res += chr(rc) if 65 <= rc <= 90 else chr(rc - 26)
            else:
                res += chr(rc) if 97 <= rc <= 122 else chr(rc - 26)
        else:
            res += c

    return res