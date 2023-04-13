ages = []
age = int(input())
while age != -1:
    ages += [age]
    age = int(input())

ages.sort()

print(ages[-1], ages[-2])