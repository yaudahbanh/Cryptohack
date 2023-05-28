from Crypto.Util.number import *
from pwn import *

enc = "73626960647f6b206821204f21254f7d694f7624662065622127234f726927756d"

pale = bytes.fromhex(enc)

for i in range(1, 100):
    iya = xor(i, pale)

    if b"crypto" in iya:
        print(iya)
        print('Found key in :', i)
        break