import random

_from = 1
_to = 99

guess = random.randint(_from,_to)
print(guess)
status = input()

while status != 'd':
    if status == 'k':
        _to = guess-1
    if status == 'b':
        _from = guess+1
    
    guess = random.randint(_from,_to)
    print(guess)
    status = input()