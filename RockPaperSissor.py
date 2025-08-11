import json
import random


class RPSGame:

    def __init__(self):
        print(
            """ 
    ========================
    Rock, Paper Scissor Game
    ========================
              """
        )
        print(
            """ 
    Rock = r
    Paper = p
    scissor = s
              """
        )
        self.choicesPossibilities = ["r", "p", "s"]
        self.permission = "n"
        self.win = 0
        self.loss = 0
        self.tries = 0
        self.match = 0

    def userTurn(self, userchoice):
        self.userchoose = userchoice
        try:
            if not self.userchoose in self.choicesPossibilities:
                print("Invalid choice")
        except Exception as error:
            print(error)
        return self.userchoose

    def botTurn(self):
        self.botchoice = random.choice(self.choicesPossibilities)
        return self.botchoice

    def choices(self):
        try:
            self.tries += 1
            if self.userchoose == self.botchoice:
                self.match += 1
                print("match tie!!!")
            elif (
                (self.userchoose == "r" and self.botchoice == "s")
                or (self.userchoose == "p" and self.botchoice == "r")
                or (self.userchoose == "s" and self.botchoice == "p")
            ):
                self.win += 1
                print("Congratulation's',You Win!!!")
                print(f"You got {self.win} points")
                print(f"Your Choice:\t\"{self.userchoose}\"\nBot Choice:\t\"{self.botchoice}\"")
            else:
                self.loss += 1
                print("You Loss!!!")
                print(f"Your Choice:\t{self.userchoose}\nBot Choice:\t{self.botchoice}")
        except Exception as error:
            print(error)

o = RPSGame()

def main():
    while (True):
        permission = input("Do You Want to Continue (y/n)\t").lower()
        try:
            if permission == "y":
                o.botTurn()
                userturn = input("Enter Your choice (r , p , s)\t")
                o.userTurn(userturn)
                o.choices()
            elif permission == "n":
                print(f""" 
                ==================================
                        ---:Result:---
                ==================================      
                Your tries {o.tries} 
                Your Win Points {o.win}
                Your tie Points {o.match}
                Your Loss Points {o.loss}
                      """)
                print("Thanks for Playing🤗")
                break
            else:
                print(ValueError("Invalid choice!!!"))
        except Exception as error4:
            print(error4)

if __name__ == "__main__":
    main()
