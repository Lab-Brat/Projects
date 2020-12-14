import sys
# import load_dictionary


def load(file):
    """Open a text file & return a list of lowercase strings."""

    try:
        with open(file) as in_file:
            # remove whitespaces and put each word on a new line
            loaded_txt = in_file.read().strip().split('\n')
            # lowercase all the words
            loaded_txt = [x.lower() for x in loaded_txt]
            
            return loaded_txt

    except IOError as e:
        print("{}\nErroropening{}.Terminatingprogram.".format(e,file), file=sys.stderr)
        sys.exit(1)


word_list = load('2of4brif.txt')
pali_list = []


for word in word_list:
    if len(word) > 1 and word == word[::-1]:
        pali_list.append(word)


print('\n')
print("Number of palindromes found = {} \n".format(len(pali_list)))
print(*pali_list, sep='\n')
