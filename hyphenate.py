word = str(input("Enter your word: "))
letter_list = []
new_word = ""
for i in word:
    letter_list.append(i)

for j in letter_list:
    if j != letter_list[-1]:
        new_word = new_word + j + "-"
    else:
        new_word += j

print(new_word)
