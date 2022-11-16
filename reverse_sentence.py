sentence = str(input("Enter your sentence: "))
list_of_words = sentence.split(" ")
new_sentence = ""

new_reversed_list = list_of_words[::-1]

for i in new_reversed_list:
    new_sentence = new_sentence + i + " "

print(new_sentence)
