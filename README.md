# RC4-drop
Sample Python 3 implementation of RC4-drop[n] (MARK-4), which discards the first n bytes of the keystream after key scheduling to improve security. An n in the range 768 <= n <= 3072 is recommended, but this implementation can also be used as regular RC4 with n = 0.

Since RC4 (including RC4-drop[n]) is widely believed to be insecure, using this implementation for non-educational purposes is not recommended. RC4 is a symmetric encryption algorithm, so you can decrypt the ciphertext by encrypting it again. Finally, there is also a helper function to help encrypt a file.

## Usage
```py
import RC4_drop

rc4 = RC4_drop.RC4("0102030405", 768) # key, offset
ciphertext_1 = rc4.cipher("0102030405", "hex", "plain") # hex plaintext, ascii ciphertext
ciphertext_2 = rc4.cipher("foo", "plain", "file") # ascii plaintext, file ciphertext
ciphertext_3 = rc4.cipher("bar", "file", "hex") # file plaintext, hex ciphertext
print(ciphertext_1, ciphertext_2, ciphertext_3)
```
