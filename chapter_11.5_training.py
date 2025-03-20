test_sentence = "This is a sentence"

"print(my_join(my_split(sentence,' '),','))"
"print(my_join(my_split(sentence,' '),'\n'))"

def my_split(sentence, where):
    word_list = []
    word = ""
    for letter in sentence:
        if letter == where:
            word_list.append(word)
            word = ""
        else:
            word += letter
    word_list.append(word)
    return word_list

def my_join(str_list, separator):
    new_sentence = ""
    for word in str_list:
        new_sentence += word
        if str_list.index(word) != len(str_list)-1 :
            new_sentence += separator
    return new_sentence

print(my_join(my_split(test_sentence,' '),','))
print(my_join(my_split(test_sentence,' '),'\n'))

print(my_split(test_sentence,' '))