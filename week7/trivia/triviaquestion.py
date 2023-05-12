import itertools
import random

class TriviaQuestion():

    def __init__(self, question, category, diffLevel, correctAns, incorrectAns, id_iter):
        self.question = question
        self.category = category
        self.diffLevel = diffLevel
        self.correctAns = correctAns
        self.incorrectAns = incorrectAns
        self.id_iter = id_iter

    def getQuestion(self):
        return self.question

    def getCategory(self):
        return self.category

    def getDiffLevel(self):
        return self.diffLevel

    def getCorrectAns(self):
        return self.correctAns

    def getIncorrectAns(self):
        return self.incorrectAns

    def getId(self):
        return self.id_iter

    def getShuffledAnswers(self):
        
        questionList = self.incorrectAns
        questionList.append(self.correctAns)
        
        random.shuffle(questionList)
        
        return questionList

    def __str__(self):
        retstr = self.question
        retstr += " "
        retstr += self.correctAns
        retstr += " "
        retstr += str(self.incorrectAns)

        return retstr
