import random

class Die():
    def __init__(self, sides = 6):
        self.sides = sides
        self.currentFaceValue = None

    def roll(self):
        self.currentFaceValue = random.randint(1, self.sides)

    def getCurrentFaceValue(self):
        if self.currentFaceValue == None:
            self.roll()
        return self.currentFaceValue

    def showDieFace(self):
        match self.currentFaceValue:
            case 1:
                return f"⚀"
            case 2:
                return f"⚁"
            case 3:
                return f"⚂"
            case 4:
                return f"⚃"
            case 5:
                return f"⚄"
            case 6:
                return f"⚅"


def check_for_yahtzee(array):
    if(array[0].getCurrentFaceValue() == array[1].getCurrentFaceValue() == 
    array[2].getCurrentFaceValue() == array[3].getCurrentFaceValue() == array[4].getCurrentFaceValue()):
        return True


def roll_five():
    joined_die = []
    listOfDice = [Die(), Die(), Die(), Die(), Die()]
    
    for die in listOfDice:
        die.roll()
        joined_die.append(die.showDieFace())
    print(" ".join(joined_die))

    if(check_for_yahtzee(listOfDice)):
        print("YAHTZEE")
    

roll_five()