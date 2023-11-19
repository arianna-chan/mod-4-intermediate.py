def shift_letter(letter, shift):
    if letter.isalpha():
        ascii_offset = ord('A') if letter.isupper() else ord('a')
        shifted_letter = chr((ord(letter) - ascii_offset + shift) % 26 + ascii_offset)
        return shifted_letter
    else:
        return letter

def caesar_cipher(message, shift):
    result = ''.join(shift_letter(char, shift) for char in message)
    return result

def shift_by_letter(letter, letter_shift):
    if letter_shift.isalpha() and letter.isalpha():
        ascii_offset = ord('A') if letter.isupper() else ord('a')
        shift = ord(letter_shift) - ascii_offset
        return shift_letter(letter, shift)
    else:
        return letter

def vigenere_cipher(message, key):
    message = message.upper()
    key = key.upper()
    if not key.isalpha():
        return "Invalid. Please do NOT use any spaces or unique characters in your key"

    result = ""
    for i, char in enumerate(message):
        result += shift_by_letter(char, key[i % len(key)])

    return result

# Test cases
print(shift_letter("A", 0))        # Output: "A"
print(shift_letter("A", 2))        # Output: "C"
print(shift_letter("Z", 1))        # Output: "A"
print(shift_letter("X", 5))        # Output: "C"
print(shift_letter(" ", "_"))      # Output: " "

print(caesar_cipher("HELLO", 3))   # Output: "KHOOR"
print(caesar_cipher("WORLD", 7))   # Output: "DUWTL"
print(caesar_cipher("SPACE", 0))   # Output: "SPACE"
print(caesar_cipher("CIPHER", 10)) # Output: "MKXOBY"

print(shift_by_letter("B", "K"))   # Output: "L"
print(shift_by_letter("D", "G"))   # Output: "C"
print(shift_by_letter("X", "A"))   # Output: "X"
print(shift_by_letter(" ", "_"))   # Output: " "

print(vigenere_cipher("A C", "KEY"))         # Output: "K A"
print(vigenere_cipher("HELLO WORLD", "KEY")) # Output: "RIJVS UYVJN"
print(vigenere_cipher("SPACE", "ABC"))        # Output: "SBUEC"
print(vigenere_cipher("ENCRYPT ME", "KEY"))   # Output: "RIJVSML UY"
