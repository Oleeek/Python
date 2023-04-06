import random


choices = ["Paper", "Rock", "Scissors"]
choose = str(input("Rock, Paper, Scissors: "))
number = random.randint(1, 2)
computerChoose = choices[number]

def main():
    if choose == "paper":
        if computerChoose == "Rock":
            print("Won")
            if computerChoose == "Paper":
                print("draw")
            if computerChoose == "Scissors":
                print("Loss")
    if choose == "Rock":
        if computerChoose == "Paper":
            print("Loss")
        if computerChoose == "Rock":
            print("Draw")
        if computerChoose == "Scissors":
            print("Won")
    if choose == "Scissors":
        if computerChoose == "Paper":
            print("Won")
            if computerChoose == "Rock":
                print("Loss")
            if computerChoose == "Scissors":
                print("Draw")

main()