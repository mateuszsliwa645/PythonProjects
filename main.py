import json
import random


def check_answer(correct_answer, answer):
    return correct_answer == answer.upper()


print("Welcome to my quiz!")

playing = input("Do you want to play my game?(Y/N)\n")

playing = playing.upper()

if playing == 'N':
    print("Goodbye then.")

else:
    remaining_questions = []

    j = open('questions.json')
    questions = json.load(j)

    print("Let's begin!\n")
    points = 0

    for i in questions['questions']:
        remaining_questions.append(i['questionNumber'])

    while remaining_questions:
        question = random.choice(remaining_questions)
        remaining_questions.remove(question)
        print("Question!")
        for i in questions['questions']:
            if i['questionNumber'] == question:

                print(i['question'])
                for k in range(len(i['answers'])):
                    print(i['answers'][k])

                answer = input("Pick answer!\n")
                if check_answer(i['correctAnswer'], answer):
                    print("Correct answer! +1 point")
                    points += 1
                else:
                    print("Wrong answer!\nCorrect answer: "+i['correctAnswer'])
    print("You have got: " + str(points)+" points!")
    j.close()










