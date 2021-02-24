input_file = open("hey.txt", "r")

text = input_file.read()
text = text.replace("\n", " ")

word_list = text.split(" ")

for word in word_list:
    word_2 = " "
word_list[word_list.index(word)] = word_2

while " i" in word_list:
    word_list.remove(" ")

word_dict = {}
for word in word_list:
    if word not in word_dict:
        word_dict[word] = 1
    else: 
        word_dict[word] +=1

for word in word_dict:
    print(format(word, "10s"), format(word_dict[word], "5d"))

input_file.close()