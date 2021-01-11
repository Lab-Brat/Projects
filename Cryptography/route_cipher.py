# initialize variables (INPUT)
ciphertext = "16 12 8 4 0 1 5 9 13 17 18 14 10 6 2 3 7 11 15 19"
COLS = 4
ROWS = 5
key = "-1 2 -3 4"
print("\nciphertext = {}".format(ciphertext))


def build_matrix(key_int, cipherlist):
    start = 0
    stop = ROWS
    translation_matrix = [None] * COLS

    # fill translation matrix
    for k in key_int:
        if k < 0:
            col_items = cipherlist[start:stop]
        elif k > 0:
            col_items = list((reversed(cipherlist[start:stop])))
        translation_matrix[abs(k)-1] = col_items
        start += ROWS
        stop += ROWS

    return translation_matrix


# print("\nciphertext = {}".format(ciphertext))
# print("\ntranslation matrix =", *translation_matrix, sep="\n")
# print("\nkey length= {}".format(len(key_int)))

def decrypt(translation_matrix):
    plaintext = ''
    # Extracting plain text
    for i in range(ROWS):
        for j in translation_matrix:
            word = str(j.pop())
            plaintext += word + ' '
    # print("\nplaintext = {}".format(plaintext))
    return plaintext


# print(main())
# cipherlist = list(ciphertext.split())
# key_int = [int(i) for i in key.split()]
# mm = build_matrix(key_int, cipherlist)

# print(*mm, sep="\n")

def main():
    # add every number separately into a list
    cipherlist = list(ciphertext.split())
    key_int = [int(i) for i in key.split()]

    translation_matrix = build_matrix(key_int, cipherlist)
    print("\ntranslation matrix =", *translation_matrix, sep="\n")
    plaintext = decrypt(translation_matrix)
    print("\ndecrypted message= {}".format(plaintext))


if __name__ == '__main__':
    main()