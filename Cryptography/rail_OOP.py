class RailFenceCipher:
    def __init__(self, text):
        self.text = text
        self.text_up = ("".join(self.text.split())).upper()

    def __repr__(self):
        return "[Result: {}]".format(self.text_up)

if __name__ == "__main__":

    plaintxt = 'Buy more Maine potatoes'
    case1 = RailFenceCipher(plaintxt)
    print(case1)
