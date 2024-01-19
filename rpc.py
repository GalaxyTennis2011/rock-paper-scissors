from tkinter import *
from random import choice

root = Tk()

choices = ["Rock", "Paper", "Scissors"]

def winner():

  
    if userChoice["text"] == robotChoice["text"]:
        winnerGame["text"] = "Tie Game!!"
    elif userChoice["text"] == "Rock" :
        if robotChoice["text"] == "Paper":
            winnerGame["text"] = "Robot won!!"
        else:
            winnerGame["text"] = "You won!!"  
    elif userChoice["text"] == "Paper":
        if robotChoice["text"] == "Rock":
            winnerGame["text"] = "User won!!"
        else:
            winnerGame["text"] = "Robot won!!"
    elif userChoice["text"] == "Scissors":
        if robotChoice["text"] == "Rock":
            winnerGame["text"] = "Robot won!!"
        else:
            winnerGame["text"] = "User won!!"
  

def rock():
    userChoice["text"] = "Rock"
    robot = choice(choices)
    robotChoice["text"] = f"{robot}"
    winner()
def paper():
    userChoice["text"] = "Paper"
    robot = choice(choices)
    robotChoice["text"] = f"{robot}"
    winner()
def scissors():
    userChoice["text"] = "Scissors"
    robot = choice(choices)
    robotChoice["text"] = f"{robot}"
    winner()

rockButton = Button(root, text="Rock", font=("Arial", 20, "bold"), height = 5, width = 10, command=rock, justify="center")
rockButton.grid(column = 5, columnspan=3, row = 1)

paperButton = Button(root, text="Paper", font=("Arial", 20, "bold"), height = 5, width = 10, command=paper, justify="center")
paperButton.grid(column = 5, columnspan=3, row = 2)

scissorButton = Button(root, text="Scissor", font=("Arial", 20, "bold"), height = 5, width = 10, command=scissors, justify = "center")
scissorButton.grid(column = 5, columnspan=3, row = 3)

userChoice = Label(root, text=f"You're choosing...", font=("Arial", 25, "bold"), height = 3, width = 15, justify = "center")
userChoice.grid(column = 5, columnspan=3, row = 4)

robotChoice = Label(root, text=f"Robot choosing...", font=("Arial", 25, "bold"), height = 3, width = 15, justify = "center")
robotChoice.grid(column = 5, columnspan=3, row = 5)

winnerGame = Label(root, text = "", font = ("Arial", 20, "bold"), height = 3, width = 15, justify = "center")
winnerGame.grid(column = 5, columnspan=3,  row = 6)

root.mainloop()