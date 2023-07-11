# made by sean devereux
# made in a little over 2 hours, as my first python project. 

from tkinter import StringVar
from tkinter import IntVar
import customtkinter 
import random
import requests
import html

customtkinter.set_appearance_mode("System")
customtkinter.set_default_color_theme("blue")

session_url = "https://opentdb.com/api_token.php?command=request"
session_token = requests.get(session_url)
session_token = session_token.json()
session_token = session_token['token']

app = customtkinter.CTk() 
app.geometry("900x240")

global mercy
mercy = 0

global score
score = IntVar()
score.set(0)

global currentQuestion 
currentQuestion = StringVar()
currentQuestion.set('hello')

global currentAnswer 
currentAnswer = StringVar()

global answersLabelText 
answersLabelText = StringVar()
#funcs
def get_question():
    global mercy
    mercy = 0
    question_url = "https://opentdb.com/api.php?amount=1&difficulty=medium&type=multiple&token=" + session_token
    quest = requests.get(question_url)
    quest = quest.json()
    for i in quest['results']:

        data = i['question']
        data = html.unescape(data)
        answer = i['correct_answer']
        answer = html.unescape(answer)
        answers = i['incorrect_answers']
        answers = html.unescape(answers)

        answers.append(answer)
        random.shuffle(answers)

        global currentQuestion
        global currentAnswer
        currentQuestion.set(data)
        currentAnswer.set(answer)
        answersLabelText.set(answers)
        #print(currentAnswer.get())
        return currentQuestion
    
def get_answer():
    global mercy
    global score
    if answerBox.get().lower() == currentAnswer.get().lower():
        print("true")
        score.set(score.get() + 1)
        get_question()
    else:
        print("false")
        mercy = mercy + 1
        if mercy > 3:
            get_question()

        score.set(score.get() - 1)

        

answersLabel = customtkinter.CTkLabel(master=app, textvariable=answersLabelText)
answersLabel.place(relx=0.5, rely=0.8, anchor=customtkinter.CENTER)

ScoreLabel = customtkinter.CTkLabel(master=app, textvariable=score)
ScoreLabel.place(relx=0.1, rely=0.3, anchor=customtkinter.CENTER)

yourScoreLabel = customtkinter.CTkLabel(master=app, text="Your score : ")
yourScoreLabel.place(relx=0.05, rely=0.3, anchor=customtkinter.CENTER)

questionLabel = customtkinter.CTkLabel(master=app, textvariable=currentQuestion)
questionLabel.place(relx=0.5, rely=0.3, anchor=customtkinter.CENTER)

answerBox = customtkinter.CTkEntry(master=app)
answerBox.place(relx=0.5, rely=0.5, anchor=customtkinter.CENTER)

button = customtkinter.CTkButton(master=app, text="Random Question", command=lambda: get_question())
button.place(relx=0.5, rely=0.1, anchor=customtkinter.CENTER)

answerButton = customtkinter.CTkButton(master=app, text="is this it?", command=lambda: get_answer())
answerButton.place(relx=0.5, rely=0.9, anchor=customtkinter.CENTER)

app.mainloop()

