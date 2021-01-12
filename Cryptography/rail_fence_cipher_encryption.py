# import time
# start = time.time()

plaintext = 'Buy more Maine potatoes'


def split_caps(txt):
    # pick plaintext apart and capitalize
    txt_up = ''
    for i in txt:
        if i!=' ':
            txt_up += i.upper()
    return txt_up

def zig_zag(txt_up):
    # split text into upper and lower parts
    split_text = [[], []]
    for j in range(len(txt_up)):
        if j%2 == 0:
            split_text[0].append(txt_up[j])
        else:
            split_text[1].append(txt_up[j])

    return split_text

def combine(split_text):
    # combine the split text together
    put_back = ''
    count = 0
    for i in range(len(split_text)):
        for j in split_text[i]:
            put_back += j
            count += 1
            if count%5 == 0:
                put_back += ' '
    return put_back


def encrypt(plaintxt):
    step1 = split_caps(plaintext)
    step2 = zig_zag(step1)
    step3 = combine(step2)
    return step3


def main():
    print("Message to be encrypted:  {}".format(plaintext))
    encryption = encrypt(plaintext)
    print("Message after enctyption: {}".format(encryption))
    
if __name__ == '__main__':
    main()

# end = time.time()
# print('time spent: ', end-start)