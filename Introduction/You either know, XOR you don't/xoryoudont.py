from pwn import *

enc = "0e0b213f26041e480b26217f27342e175d0e070a3c5b103e2526217f27342e175d0e077e263451150104"

pale = bytes.fromhex(enc)

# format = "crypto{"
# okok = xor(format, pale[:7]) (looking for the key)

key = "myXORkey"

flag = []

for i in range(len(pale)):
    flag.append(xor(pale[i], key[i % len(key)]))

print("".join(iya.decode() for iya in flag))