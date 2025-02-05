#RPS.py
#Name:
#Date:
#Assignment:
import random

def main():
  wins = 0
  ties = 0
  losses = 0
  #Create a loop that continues as long as the user wants to play.
  play = "Y"
  while play == "Y":

  #User can play as many games as they wish.

  #Randomly choose the computer between 'R', 'P', or 'S'
  #Prompt the user for their RPS selection
    player = input("Enter choice (R/P/s): ")

  #Determine winner and state what happened to the user
    options = ["R", "P", "s"]
    computer = random.choice(["R", "P", "s"])
    if computer == "R":
      print("Computer chose Rock.")
    elif computer == "P":
      print("Computer chose Paper.")
    else:
      print("Computer chose Scissors.")

    if player == computer:
      print ("Tie!")
      ties = ties + 1
    elif player == "R" and computer == "s":
      print ("You win!")
      wins = wins + 1
    elif player == "R" and computer == "P":
      print ("You lose!")
      losses = losses + 1
    elif player == "P" and computer == "R":
      print ("You win!")
      wins = wins + 1
    elif player == "P" and computer == "s":
      print ("You lose!")
      losses = losses + 1
    elif player == "s" and computer == "R":
      print ("You lose!")
      losses = losses + 1
    elif player == "s" and computer == "P":
      print ("You win!")
      wins = wins + 1
    else:
      print ("That's not an option, you nitwit. Follow the prompt.")
  

  #Ask the user if they would like to play again.
    play = input("Would you like to play again (Y/N)? ")

  #In the end, print the stats
  print("Wins \t Ties \t Losses")
  print("---- \t ---- \t ------")
  print(wins, "\t", ties , "\t", losses)

if __name__ == '__main__':
  main()
