class RC4:
    def __init__(self, key, n):
        self.key = [ord(char) for char in key]
        self.s = self.KSA(self.key)
        self.n = n

    def KSA(self, key):
        state = [i for i in range(256)]
        j = 0
        l = len(key)
        for i in range(256):
            j = (j + state[i] + key[i % l]) % 256
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
        to_convert = open(file, "r")
        return to_convert.read()

    def cipher(self, plaintext):
        plaintext = [ord(char) for char in plaintext]
        keystream = self.PRGA()
        for i in range(self.n):
            next(keystream)
        ciphertext = [plaintext[i] ^ next(keystream) for i in range(len(plaintext))]
        return "".join([hex(char)[2:] for char in ciphertext])
