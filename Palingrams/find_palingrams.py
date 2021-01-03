"""Find all word­pair palingrams in a dictionary file."""
import load_dictionary
import time
start_time = time.time()

word_list = load_dictionary.load('2of4brif.txt')

# find word­pair palingrams
def find_palingrams():
    """Find dictionary palingrams."""
    pali_list = []
    wl_set = set(word_list) #computing sets is much faster, 0.44s compared to 145.53
    
    for word in wl_set:
        end = len(word)
        rev_word = word[::-1]
        
        if end > 1:
            for i in range(end):
                if word[i:] == rev_word[:end-i] and rev_word[end-i:] in wl_set:
                    pali_list.append((word, rev_word[end-i:]))
                if word[:i] == rev_word[end-i:] and rev_word[:end-i] in wl_set:
                    pali_list.append((rev_word[:end-i], word))
                    
    return pali_list
                
palingrams = find_palingrams()

# sort palingrams on first word
palingrams_sorted = sorted(palingrams)

# display list of palingrams
print("\nNumber of palingrams = {}\n".format(len(palingrams_sorted)))

pals = []
for first, second in palingrams_sorted:
    # print("{} {}".format(first, second))
    pals.append(str(first)+' '+str(second))

MyList = []
for i in pals:
    MyList.append(i)


# Print all palingrams to a txt file
MyFile=open('palingrams.txt', 'w')
MyList=map(lambda x:x+'\n', MyList)
MyFile.writelines(MyList)
MyFile.close()


end_time = time.time()
print("Runtime for this program was {} seconds.".format(end_time - start_time))