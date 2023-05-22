# Brute force the shift of caesar cipher from 1 to 100 

def decode(text, shift):
    plaintext = ""
    for char in text:
        if char.isalpha():
            ascii_offset = ord('a') if char.islower() else ord('A')
            decode_char = chr((ord(char) - ascii_offset - shift) % 26 + ascii_offset)
        else:
            decode_char = char
        plaintext = plaintext + decode_char
    return plaintext

cipher = "YOUR CAESAR CIPHER HERE"

for i in range(1, 100):
    decodeme = decode(cipher, i)
    print(decodeme)
