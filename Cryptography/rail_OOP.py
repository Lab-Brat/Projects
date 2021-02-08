class RailFenceCipher:
    """
    Input: A string that you wish to encrypt or dencryption
    Output: An encrypted or decrypted string
    """
    def __init__(self, text):
        self.text = text
        self.split_text = [None] * 2
        self.text_up = ("".join(self.text.split())).upper()
        self.text_low = ("".join(self.text.split())).lower()

    def encrypt(self):
        """Split the string in a zig-zag fashion, then put it back
           together with spaces at every 5 character mark """
        upper_part = self.text_up[0::2]
        lower_part = self.text_up[1::2]
        result = upper_part + lower_part

        return ' '.join([result[i:i+5] for i in range(0, len(result), 5)])

    def decrypt(self):
        """Split the string into two halves, then add a character
           from each string on every iterationv (reverse of zig-zag)"""
        half = len(self.text_low)//2
        left_part = self.text_low[0:half]
        right_part = self.text_low[half:len(self.text_low)]

        result = ''
        for i in range(half):
            result += left_part[i]
            result += right_part[i]

        return result

    def __repr__(self):
        return "[Result: {}]".format(self.text_low)


if __name__ == "__main__":

    plaintxt = 'Buy more Maine potatoes'
    plaintxt2 = "BYOEA NPTTE UMRMI EOAOS"

    case1 = RailFenceCipher(plaintxt)
    case2 = RailFenceCipher(plaintxt2)

    print("After encryption:  {}".format(case1.encrypt()))
    print("After dencryption: {}".format(case2.decrypt()))
