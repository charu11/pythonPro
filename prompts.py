from mcq import Question
import time

question_prompt = [
    "who is the father of the biology?\n(a) einstein\n(b) aristotal\n(c) thompson\n\n",
    "who is the father of the science?\n(a) einstein\n(b) gallili\n(c) isaac newton\n\n",
    "who is the father of the biochemistry?\n(a) sir. pablo escobar\n(b) neuberg\n(c) anselme payen\n\n"
]


questions = [
    Question(question_prompt[0], "b"),
    Question(question_prompt[1], "b"),
    Question(question_prompt[2], "b")

]


def countdown(n):
    while n > 0:
        run_test(questions)
        n = n-1
        if n == 0:
            print("time is up")
        countdown(10)

def run_test(questions):
    score = 0
    for question in questions:
        answer = input(question.prompt)
        if answer == question.answer:
            score += 1

    print("hey weddi you got " + str(score) + " out of " + str(len(questions)) + " correct" )

countdown(10)