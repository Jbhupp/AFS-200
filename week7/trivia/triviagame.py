class TriviaGame():
    def __init__(self):
        self.questions = []
    def addQuestions(self, question):
        self.questions.append(question)

    def getAllQuestions(self):
        # to retrieve all questions
        return self.questions