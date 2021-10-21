class RC4:
    """
    Sample Python 3 implementation of RC4-drop[n] (MARK-4).
    """

    def __init__(self, key, n=0):
        self.key = list(bytearray.fromhex(key))
        self.s = self.KSA(self.key)
        self.n = n

    def KSA(self, key):
        state = [i for i in range(256)]
        j = 0
        for i in range(256):
            j = (j + state[i] + key[i % len(key)]) % 256
            state[i], state[j] = state[j], state[i]
        return state

    def PRGA(self):
        i = 0
        j = 0
        while True:
            i = (i + 1) % 256
            j = (j + self.s[i]) % 256
            self.s[i], self.s[j] = self.s[j], self.s[i]
            k = self.s[(self.s[i] + self.s[j]) % 256]
            yield k

    def convert_file(self, file):
        with open(file, "r") as data:
            return data.read()

    def write_file(self, data):
        with open("data", "w") as file:
            file.write(data)

    def cipher(self, plaintext, in_format="plain", out_format="plain"):
        if in_format == "plain":
            pass
        elif in_format == "hex":
            plaintext = bytearray.fromhex(plaintext).decode()
        elif in_format == "file":
            plaintext = self.convert_file(plaintext)
        else:
            raise NotImplementedError

        plaintext = list(map(ord, plaintext))
        keystream = self.PRGA()
        for i in range(self.n):
            next(keystream)
        ciphertext = [plaintext[i] ^ next(keystream) for i in range(
            len(plaintext))]

        if out_format == "plain":
            return "".join(map(chr, ciphertext))
        elif out_format == "hex":
            return bytes(ciphertext).hex()
        elif out_format == "file":
            self.write_file("".join(map(chr, ciphertext)))
            return "data"
        else:
            raise NotImplementedError
