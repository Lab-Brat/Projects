class RailFenceCipher:
    def __init__(self, text):
        self.text = text
        self.split_text = [None] * 2
        self.text_up = ("".join(self.text.split())).upper()
        self.text_low = ("".join(self.text.split())).lower()

    def encrypt(self):
        upper_part = self.text_up[0::2]
        lower_part = self.text_up[1::2]
        result = upper_part + lower_part

        return ' '.join([result[i:i+5] for i in range(0, len(result), 5)])

    # def decrypt(self):

    def __repr__(self):
        return "[Result: {}]".format(self.text_low)


if __name__ == "__main__":

    plaintxt = 'Buy more Maine potatoes'
    plaintxt2 = "BYOEA NPTTE UMRMI EOAOS"

    case1 = RailFenceCipher(plaintxt)
    case2 = RailFenceCipher(plaintxt2)

    # print(case1.encrypt())
    print(case2)
