# Evaluation about Base64 challenge as Introduction on Cryptohack.org

import base64

text = "crypto/Base+64+Encoding+is+Web+Safe/"

decode = base64.b64decode(text)
tohex = decode.hex()

print(tohex)