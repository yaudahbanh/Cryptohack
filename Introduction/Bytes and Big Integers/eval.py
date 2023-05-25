# Evaluation about Bytes and Big Integers challenge as Introduction on Cryptohack.org

from Crypto.Util.number import *

text = "crypto{3nc0d1n6_4ll_7h3_w4y_d0wn}"
bytes = text.encode()

print(bytes_to_long(bytes))