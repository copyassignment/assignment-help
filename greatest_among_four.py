n = 4
list_of_numbers = []  

for i in range(n):
    list_of_numbers.append(int(input(f"Enter {i+1}th number: ")))

max_number = list_of_numbers[0]

for i in list_of_numbers:
    if i > max_number:
        max_number = i

print(max_number)
