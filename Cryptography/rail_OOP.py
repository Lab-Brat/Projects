class RailFenceCipher:
    def __init__(self, text):
        self.text = text
        self.split_text = [None] * 2
        self.text_up = ("".join(self.text.split())).upper()

    def __repr__(self):
        return "[Result: {}]".format(self.text_up)

    def encrypt(self):
        upper_part = self.text_up[0::2]
        lower_part = self.text_up[1::2]
        result = upper_part + lower_part

        return ' '.join([result[i:i+5] for i in range(0, len(result), 5)])


if __name__ == "__main__":

    plaintxt = 'Buy more Maine potatoes'
    case1 = RailFenceCipher(plaintxt)
    print(case1.encrypt())
