def DivisorCount(num):
    divisor_count = 0
    for i in range(1, num+1):
        if (num % i == 0):
            divisor_count += 1
    return divisor_count

num = int(input())
max_divisor_count_num = num

for i in range(19):
    num = int(input())
    if (DivisorCount(num) > DivisorCount(max_divisor_count_num)):
        max_divisor_count_num = num
    elif (DivisorCount(num) == DivisorCount(max_divisor_count_num) and num > max_divisor_count_num):
        max_divisor_count_num = num

print(max_divisor_count_num, DivisorCount(max_divisor_count_num))