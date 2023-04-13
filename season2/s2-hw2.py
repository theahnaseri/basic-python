def DivisorCount(num):
    divisor_count = 0
    for i in range(1, num+1):
        if (num % i == 0):
            divisor_count += 1
    return divisor_count

num = int(input())

if (DivisorCount(num) == 2):
    print("prime")
else:
    print("not prime")