from main import question_bank

start = 1
points = 0
max_points = 0

for question in question_bank:
    answer = input(f"Q.{start}: {question.text} (True/False)?: ")
    max_points += 1
    if answer == question.answer:
        points += 1
        print(f"Right answer: Points {points}/{max_points}\n\ndf")
    else:
        print(f"Wrong answer: Points {points}/{max_points}\n\n")
    start += 1

print(f"Congrats. Final points {points}/{max_points}")