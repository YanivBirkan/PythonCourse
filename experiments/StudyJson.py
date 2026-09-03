import json

with open("question.json","r") as file:
    content = file.read()

data = json.loads(content)
score = 0
for question in data:
    print(question["question_text"])
    for index, alternative in enumerate(question["alternatives"]):
        print(index+1,"-" , alternative)
    user_answer = int(input("Answer:"))
    question["user_choice"]=user_answer

for index, question in enumerate(data):
    if question["user_choice"] == question["correct_answer"]:
        score+=1
        result = "Correct answer"
    else:
        result = "Wrong answer"
    message = f"{result} in question - {index+1}:  You answered {question['user_choice']}, " \
              f" correct answer is {question['correct_answer']}"
    print(message)
print("Score:",score)