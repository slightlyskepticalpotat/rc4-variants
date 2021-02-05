# RC4-drop
Sample Python 3 implementation of RC4-drop[n] (MARK-4), which discards the first n bytes of the keystream after key scheduling to improve security. An n in the range 768 <= n <= 3072 is recommended, but this implementation can also be used as regular RC4 with n = 0.

Since RC4 (including RC4-drop[n]) is widely believed to be insecure, using this implementation for non-educational purposes is not recommended. RC4 is a symmetric encryption algorithm, so you can decrypt the ciphertext by encrypting it again. Finally, there is also a helper function to help encrypt a file.

## Usage
```py
import RC4_drop
rc4 = RC4_drop.RC4("foo", 768) # foo is the key, n = 768
ciphertext = rc4.cipher("bar") # bar is the plaintext
print(ciphertext) # prints the ciphertext in hex format
```
