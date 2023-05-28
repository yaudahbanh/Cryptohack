# Solver XOR Properties Introduction Cryptohack.org

from pwn import xor

k1 = "a6c8b6733c9b22de7bc0253266a3867df55acde8635e19c73313"
k1_k2 = "37dcb292030faa90d07eec17e3b1c6d8daf94c35d4c9191a5e1e" # k2 = k1 ^ (k1 ^ k2)
k2_k3 = "c1545756687e7573db23aa1c3452a098b71a7fbf0fddddde5fc1" # k3 = k2 ^ (k2 ^ k3)
flag_k123 = "04ee9855208a2cd59091d04767ae47963170d1660df7f56f5faf" # flag = k123 ^ (flag ^ k123)

hexk1 = bytes.fromhex(k1)

key2 = xor(hexk1, bytes.fromhex(k1_k2))
key3 = xor(key2, bytes.fromhex(k2_k3))
k123 = xor(key2, xor(hexk1, key3))

flag = xor(k123, bytes.fromhex(flag_k123))

print(flag.decode('utf-8'))