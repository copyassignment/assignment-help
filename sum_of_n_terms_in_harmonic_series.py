n = int(input("How many terms do you want to sum in a harmonic series? "))
round_off = int(input("How many decimal points do you want to round off too? "))
total_sum = 0

for i in range(1, n + 1):
    total_sum += (1 / i)

print(int(total_sum * (10 ** round_off)) / (10 ** round_off))
