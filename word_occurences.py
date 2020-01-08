from operator import itemgetter
word_to_quantity = {}
word_list = []
word_list_2 = []
quantity_list = []
new_string_list = []
quantity = 1
sentence = str(input("Input a string of sentence."))
sentence_split = sentence.split()
for word in sentence_split:
    word_list.append(word)
for i in range (1, len(word_list)+1):
    if word_list[i-1] not in word_to_quantity:
        content = {word_list[i-1]:quantity}
        word_to_quantity.update(content)
    else:
        new_quantity = word_to_quantity[word_list[i-1]]
        content = {word_list[i-1]:new_quantity+1}
        word_to_quantity.update(content)
for key, value in sorted(word_to_quantity.items()):
    print("{} : {}".format(key,value))

