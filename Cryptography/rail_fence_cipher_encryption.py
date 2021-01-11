plaintext = 'Buy more Maine potatoes'
text_up = ''

for i in plaintext:
    if i!=' ':
        text_up += i.upper()

split_text = [[], []]
for j in range(len(text_up)):
    if j%2 == 0:
        split_text[0].append(text_up[j])
    else:
        split_text[1].append(text_up[j])

put_back = ''
count = 0
for i in range(len(split_text)):
    for j in split_text[i]:
        put_back += j
        count += 1
        if count%5 == 0:
            put_back += ' '


print(put_back)