first = int(input("Magnitude of first earchquake: "))
second = int(input("Magnitude of second earchquake: "))

difference = abs(second-first)

difference_in_energy = 32 ** difference

print(difference_in_energy)
