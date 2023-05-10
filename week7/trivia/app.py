from flask import Flask, request, render_template
import requests
import json
from socket import timeout
from urllib import response
from triviagame import TriviaGame 
from triviaquestion import TriviaQuestion
import itertools

def getData(triviaQuestions):
    URL = "https://opentdb.com/api.php?amount=7&category=27&type=multiple"

    try:
        response = requests.get(URL, timeout=25)
        response.raise_for_status()
        response_JSON = response.json()
        return response_JSON

    except requests.exceptions.HTTPError as errc:
        print(errc)
    except requests.exceptions.ConnectionError as errc:
        print(errc)
    except requests.exceptions.Timeout as errt:
        print(errt)
    except requests.exceptions.RequestException as err:
        print(err)
    print(triviaQuestions, "line 27 print")


theTriviaGame = TriviaGame()

jsonData = getData("triviaQuestions")

idCounter = 0

for data in jsonData["results"]:
    question = data["question"]
    correctAns = data["correct_answer"]
    incorrectAns = data["incorrect_answers"] 
    category = data["category"]
    diffLevel = data["difficulty"]
    id_iter = idCounter

    newQuestion = TriviaQuestion(question, category, diffLevel, correctAns, incorrectAns, id_iter)
    
    theTriviaGame.addQuestions(newQuestion) 
    idCounter += 1

theTriviaGame.getAllQuestions()

app = Flask(__name__)

@app.route("/")
def home():
    myTrivia = theTriviaGame.getAllQuestions()
    
    return render_template("displayQuestions.html", results = myTrivia)
    
@app.route("/score", methods = ["POST"])
def getScore():
    myTrivia = theTriviaGame.getAllQuestions()
    correctQuestion = []
    incorrectQuestion = []
    for question in myTrivia:

        inputValue = request.form.get(str(question.id_iter))

        if(inputValue == question.correctAns):
            correctQuestion.append(question)
        else:
            incorrectQuestion.append(question)

    results = {"correct": correctQuestion, "incorrect": incorrectQuestion}
    return render_template('answers.html', results = results)

if __name__ == "__main__":
    app.run()