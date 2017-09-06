new_list = []
word_list = ['hello','world','my','name','is','Anna']
char = 'o'

for word in word_list:
    if word.count(char):
        new_list.append(word)

print new_list

