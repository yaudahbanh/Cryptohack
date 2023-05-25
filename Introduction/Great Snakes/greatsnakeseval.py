# Evaluation about great snakes challenge as Introduction on Cryptohack.org
# xor_key = 0x32

text = "crypto{z3n_0f_pyth0n}"

a = [ord(pale) ^ 0x32 for pale in text]
print(a)