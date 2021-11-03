# RC4-variants
Sample Python 3 implementation of various RC4 variants, including regular RC4 (ARC4), RC4A, and RC4-drop[n] (MARK-4). RC4A uses two state arrays and keys instead as one, whereas RC4-drop[n] discards the first n bytes of the keystream after key scheduling to improve security. A n in the range 768 <= n <= 3072 is recommended, while n = 0 corresponds to regular RC4.

Currently, supported forms of input and output include plain text, hexadecimal text (without an 0x), and files.

Since RC4 (including RC4A and RC4-drop[n]) is widely believed to be insecure, using this implementation for non-educational purposes is not recommended. If you must, RC4-drop[n] with n = 3072 or RC4A should be more secure than RC4.

All included variants of RC4 are symmetric encryption algorithms, so you can decrypt the ciphertext by encrypting it again.

## Usage
```py
import RC4

rc4 = RC4.RC4("0102030405", 768) # key, offset
ciphertext_1 = rc4.cipher("0102030405", "hex", "plain") # hex plaintext, ascii ciphertext
ciphertext_2 = rc4.cipher("foo", "plain", "file") # ascii plaintext, file ciphertext
ciphertext_3 = rc4.cipher("bar", "file", "hex") # file plaintext, hex ciphertext
print(ciphertext_1, ciphertext_2, ciphertext_3)
rc4a = RC4.RC4A("0102030405") # key
ciphertext_4 = rc4a.cipher("0102030405", "hex", "plain") # hex plaintext, ascii ciphertext
ciphertext_5 = rc4a.cipher("foo", "plain", "file") # ascii plaintext, file ciphertext
ciphertext_6 = rc4a.cipher("bar", "file", "hex") # file plaintext, hex ciphertext
print(ciphertext_4, ciphertext_5, ciphertext_6)
```
