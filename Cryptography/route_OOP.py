class RouteCipher:
    def __init__(self, cipher, cols, rows, key):
        self.cipher = cipher
        self.cols = cols
        self.rows = rows
        self.key = key

    def prep(self):
        self.cipherlist = list(self.cipher.split())
        self.key_int = [int(i) for i in self.key.split()]

    def __repr__(self):
        # return '[decryption info: {}, {}, {}]'.format(\
        #                          self.cols, self.rows, self.key)
        return '[prep result: {}, {}]'.format(\
                                   self.cipherlist, self.key_int)

ciphertext = "16 12 8 4 0 1 5 9 13 17 18 14 10 6 2 3 7 11 15 19"
COLS = 4
ROWS = 5
KEY = "-1 2 -3 4"

dec1 = RouteCipher(ciphertext, COLS, ROWS, KEY)
dec1.prep()
print(dec1)
