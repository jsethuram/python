def word_mixer(words_list):
    sorted_list = sorted(words_list)
    sorted_list_len = len(sorted_list)
    new_words = []
    while sorted_list_len > 5:
        new_words.append(sorted_list.pop(-5))
        sorted_list_len = sorted_list_len - 1
        new_words.append(sorted_list.pop(0))
        sorted_list_len = sorted_list_len - 1
        new_words.append(sorted_list.pop(-1))
        sorted_list_len = sorted_list_len - 1    
    return new_words

word = input("Enter a Poem : ")
word_list = word.split(" ")
word_list_len = len(word_list)
new_list = []

for i in range(0,word_list_len):
    word_len = 0
    word_len = len(word_list[i])
    
    if word_len <= 3:
        new_list.append(word_list[i].lower())
        
        
    elif word_len >= 7:
        new_list.append(word_list[i].upper())
        
    else:
        new_list.append(word_list[i])
        

new_list = word_mixer(new_list)
print(" ".join(new_list))
