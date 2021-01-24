with open('input.txt', 'r') as file:
    data = file.read().replace('\n', '')

b = 1
count = 1 
cod = ""

if data[0] != ' ':
    cod += '@'

# ord --> letters to ascii
# chr --> ascii to letters

for i in range(1, len(data)):
    if data[i] == data[i-1]:
        count += 1
    else:
        char = chr(64+count)
        count = 1
        cod += char

print(cod, file=open("output.txt", "a"))
