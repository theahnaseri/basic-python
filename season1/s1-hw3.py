number = input()

size = len(number)
reversed_number = ""

for i in range(size):
    reversed_number += number[size-i-1]

res = int(reversed_number)*2
print(res)