from itertools import permutations
from itertools import product

class RouteCipher:
    """
    Input: cipher: Either an encrypted or decrypted string
           cols, rows: Dimentions of the encryption table
           key: A key that specifies how to read data from the matrix
    Output: Either an encrypted or decrypted string
    """

    def __init__(self, cipher, key):
        self.cipher = cipher
        self.cols = int(list(key.keys())[0][0])
        self.rows = int(list(key.keys())[0][1])
        self.key = key[list(key.keys())[0]]
        self.cipherlist = list(self.cipher.split())
        self.key_int = [int(i) for i in self.key.split()]
        self.translation_matrix = [None] * self.cols

    def decrypt(self):
        """ Decrypts the message when called, and outputs a string"""
        start = 0
        stop = self.rows

        # create translation matrix
        for k in self.key_int:
            if k < 0:
                col_items = self.cipherlist[start:stop]
            elif k > 0:
                col_items = list((reversed(self.cipherlist[start:stop])))
            self.translation_matrix[abs(k)-1] = col_items
            start += self.rows
            stop += self.rows

        plaintext = ''
        # read translation matrix as string
        for i in range(self.rows):
            for j in self.translation_matrix:
                word = str(j.pop())
                plaintext += word + ' '
        return plaintext


    def encrypt(self):
        """ Ecrypts the message when called, and outputs a string"""
        # create translation matrix
        for i in range(self.cols):
            if self.key_int[i] < 0:
                col_items = list(reversed(self.cipherlist[i::self.cols]))
            elif self.key_int[i] > 0:
                col_items = self.cipherlist[i::self.cols]
            self.translation_matrix[i] = col_items

        plaintext = ''
        # read translation matrix as string
        for j in self.translation_matrix:
            for el in j:
                plaintext += el + ' '

        return plaintext

    def gen_all(self):
        result = []
        columns = [x for x in range(1, self.cols+1)]

        for perm in permutations(columns):
            for signs in product([1, -1], repeat=len(columns)):
                # multiply the signes to the permutations
                result.append([i*sign for i, sign in zip(perm, signs)])

        return len(result)

    def __repr__(self):
        return "[INFO]\ncipher: {}\nkey: {}".format(\
                                   self.cipher, self.key_int)


if __name__ == "__main__":
    ciphertext = "16 12 8 4 0 1 5 9 13 17 18 14 10 6 2 3 7 11 15 19"
    to_ciph = "0 1 2 3 4 5 6 7 8 9 10 11 12 13 14 15 16 17 18 19"
    KEY = {'45': "-1 2 -3 4"}

    dec1 = RouteCipher(ciphertext, KEY)
    # print("After decryption: {}".format(dec1.decrypt()))
    # print('\n')
    #
    # dec2 = RouteCipher(to_ciph, KEY)
    # print("After ecryption:  {}".format(dec2.encrypt()))
    # print('\n')
    #
    # print(dec1)

    print(dec1.gen_all())
