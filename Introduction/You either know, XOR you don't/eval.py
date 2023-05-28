from pwn import xor

text = "crypto{1f_y0u_Kn0w_En0uGH_y0u_Kn0w_1t_4ll}"

key = "myXORkey"

enc = []

for i in range(len(text)):
    enc.append(xor(text[i], key[i % len(key)]))

print("".join(iya.hex() for iya in enc))
#0e0b213f26041e480b26217f27342e175d0e070a3c5b103e2526217f27342e175d0e077e263451150104