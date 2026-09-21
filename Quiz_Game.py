# Day   project
# 5     Quiz Game

print("////////////QUIZ STARTS/////////////")
print("For every correct answer +1 and wrong answer -1")
score = 0

ques_list = ["What is the capital of Australia?","How many planets are in our Solar System?","Who wrote Romeo and Juliet?"]

ans_list = ["canberra","8","william shakespeare"]

for i in range(len(ques_list)):
    print(ques_list[i])
    ans = input("enter ans:")
    if ans.lower() == ans_list[i]:
        print("correct answer")
        score += 1
    else:
        print("wrong answer")
        score -= 1
print("Your final score is =",score)