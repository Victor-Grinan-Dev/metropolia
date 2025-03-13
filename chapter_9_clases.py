
# 1
class Player1:
    team = "Blue"
    points = 300

def main1():
    juan = Player1()
    print("The "+ juan.team +" contender has "+ str(juan.points) +" points!")

# 2
class Player2:
    _teamcolor = "Blue"
    _points = 0

    def tellscore(self):
        print(f"I am {self._teamcolor}, we have {self._points} points!")

    def goal(self):
        self._points += 1

def main2():
    juan = Player2()
    juan.goal()
    juan.tellscore()

# 3
class Player3:
    "Player-class: stores data on team colors and points."

    def __init__(self):
        self._teamcolor = input("What color do I get?: ")
        self._score = 0

    def goal(self):
        self._score += 1

    def tellscore(self):
        print(f"I am {self._teamcolor}, we have {self._score} points!")

def main():
    person1 = Player3()
    person2 = Player3()

    person1.goal()
    person1.goal()
    person2.goal()

    person1.tellscore()
    person2.tellscore()

# 4

class Customer:
    name = "John Johnsson"
    total = 1000
    paymenttype = "Masterexpress"
    number = "1234-5678-9012345"

    def printout(self):
        print("Name: ", self.name)
        print("Total: ", self.total)
        print("Payment type: ", self.paymenttype)
        print("Card/Bill number: ", self.number)


# Put your code here
class ManageCustomer(Customer):

    def addbill(self):
        self.total += 50

    def payment(self):
        self.total -= 100


def main4():
    person = ManageCustomer()
    person.name = "Homer Griffin"
    person.addbill()
    person.payment()
    person.payment()
    person.printout()