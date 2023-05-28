from pwn import xor

text = "crypto{0x10_15_my_f4v0ur173_by7e}"
enc = xor(text, 16)
enc = enc.hex().encode()

print(enc)
#73626960647f6b206821204f21254f7d694f7624662065622127234f726927756d