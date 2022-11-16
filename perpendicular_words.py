my_string = "ADG BEH CFI"

list_words = my_string.split(" ")
list_letters = []

for i in list_words:
    list_letters.append([*i])

for i in range(len(list_words)):
    s = ""
    for j in range(len(list_words[i])):
        s = s + list_letters[j][i]
    print(s)
