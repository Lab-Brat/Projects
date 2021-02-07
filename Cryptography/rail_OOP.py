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

        self.split_text[0] = upper_part
        self.split_text[1] = lower_part

        result = upper_part + lower_part

        return result

if __name__ == "__main__":

    plaintxt = 'Buy more Maine potatoes'
    case1 = RailFenceCipher(plaintxt)
    print(case1.encrypt())
