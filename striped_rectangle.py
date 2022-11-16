n = int(input("How many rows? "))
m = int(input("How many columns? "))

pluses = "+"
minuses = "-" 

for i in range(1, n+1):
        if i % 2 != 0:
            print(pluses * m)
        elif i % 2 == 0:
            print(minuses * m)
