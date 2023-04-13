score_sum = 0
win_count = 0

for i in range(30):
    score = int(input())
    score_sum += score
    if (score == 3):
        win_count += 1

print(score_sum, win_count)