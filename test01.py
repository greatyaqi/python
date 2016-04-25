import random

score = [random.randint(0,100) for i in range(40)]

print(score)

num = len(score)
sum_score = sum(score)

ave_score = sum_score/num

i = [i for i in score if i<ave_score]

print(i)

less_score = len(i)

print("the average score is:{:.1f}".format(ave_score))

print(sorted(score, reverse = True))