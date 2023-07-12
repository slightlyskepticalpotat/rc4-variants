"""Identify RC4 compared to random and RC4A output with the ciphertext's second byte"""

import secrets
import RC4

# random
zeroes = 0
for i in range(65536):
    secret = secrets.token_bytes(4)
    if int(secret[1]) == 0:
        zeroes += 1
print("Random")
print(f"Expected: 256")
print(f"Reality: {zeroes}")
print(f"Deviation: {(zeroes - 256)/256:.0%}")

# rc4a
zeroes = 0
for i in range(65536):
    secret = secrets.token_hex(16)
    rc4a = RC4.RC4A(secret)
    ciphertext = bytes.fromhex(rc4a.cipher("Hello World", "plain", "hex"))
    if rc4a.keystream_used[1] == 0:
        zeroes += 1
print("RC4A")
print(f"Expected: 256")
print(f"Reality: {zeroes}")
print(f"Deviation: {(zeroes - 256)/256:.0%}")

# rc4
zeroes = 0
for i in range(65536):
    secret = secrets.token_hex(16)
    rc4 = RC4.RC4(secret)
    ciphertext = bytes.fromhex(rc4.cipher("Hello World", "plain", "hex"))
    if rc4.keystream_used[1] == 0:
        zeroes += 1
print("RC4")
print(f"Expected: 256")
print(f"Reality: {zeroes}")
print(f"Deviation: {(zeroes - 256)/256:.0%}")
