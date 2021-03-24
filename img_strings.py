string, array = "Abram is loving to eat", []

limit = len(string) // 5

for time in range(limit):
    array.append(string[time*5: (time + 1) * 5])

print(array)