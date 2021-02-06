class RouteCipher:
    def __init__(self, cipher, cols, rows, key):
        self.cipher = cipher
        self.cols = cols
        self.rows = rows
        self.key = key
        self.cipherlist = list(self.cipher.split())
        self.key_int = [int(i) for i in self.key.split()]

    def decrypt(self):
        start = 0
        stop = self.rows
        translation_matrix = [None] * self.cols

        # create translation matrix
        for k in self.key_int:
            if k < 0:
                col_items = self.cipherlist[start:stop]
            elif k > 0:
                col_items = list((reversed(self.cipherlist[start:stop])))
            translation_matrix[abs(k)-1] = col_items
            start += self.rows
            stop += self.rows

        plaintext = ''
        # read translation matrix as string
        for i in range(self.rows):
            for j in translation_matrix:
                word = str(j.pop())
                plaintext += word + ' '
        return plaintext


    def encrypt(self):
        translation_matrix = [None] * self.cols

        # create translation matrix
        for i in range(4):
            if self.key_int[i] < 0:
                col_items = list(reversed(self.cipherlist[i::4]))
            elif self.key_int[i] > 0:
                col_items = self.cipherlist[i::4]
            translation_matrix[i] = col_items

        plaintext = ''
        # read translation matrix as string
        for j in translation_matrix:
            for el in j:
                plaintext += el + ' '

        return plaintext


    def __repr__(self):
        return '[prep result: {}, {}]'.format(\
                                   self.cipherlist, self.key_int)


ciphertext = "16 12 8 4 0 1 5 9 13 17 18 14 10 6 2 3 7 11 15 19"
to_ciph = "0 1 2 3 4 5 6 7 8 9 10 11 12 13 14 15 16 17 18 19"
COLS = 4
ROWS = 5
KEY = "-1 2 -3 4"

# dec1 = RouteCipher(ciphertext, COLS, ROWS, KEY)
# print(dec1.decrypt())

dec2 = RouteCipher(to_ciph, COLS, ROWS, KEY)
print(dec2.encrypt())
