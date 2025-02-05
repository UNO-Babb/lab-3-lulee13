#RPS.py
#Name:
#Date:
#Assignment:
import random

def main():
  wins = 0
  ties = 0
  losses = 0
  cRock = 0
  cPaper = 0
  cScissors = 0
  pRock = 0
  pPaper = 0
  pScissors = 0

  options = ["R", "P", "S"]
  #Create a loop that continues as long as the user wants to play.
  print("Welcome to Rock, Paper, Scissors!")
  player = "nothinglol"
  while player != "END":

  #User can play as many games as they wish.

  #Randomly choose the computer between 'R', 'P', or 'S'
  #Prompt the user for their RPS selection
    player = input("Enter choice (R/P/S), 'END' to stop playing, or 'STATS' to view stats: ")
    
  #Determine winner and state what happened to the user
    
    
    if player != "S" and player != "R" and player != "P" and player != "END" and player != "STATS":
      print ("That's not an option.")
    else:
      if player == "STATS":
        print("Current Stats:")
        print("Wins \t Ties \t Losses")
        print("---- \t ---- \t ------")
        print(wins, "\t", ties , "\t", losses)
        print(" ")
        print("Player Choices:")
        print("Rock \t Paper \t Scissors")
        print("---- \t ---- \t ------")
        print(pRock, "\t", pPaper, "\t", pScissors)
        print(" ")
        print("Computer Choices:")
        print("Rock \t Paper \t Scissors")
        print("---- \t ---- \t ------")
        print(cRock, "\t", cPaper, "\t", cScissors)

      computer = random.choice(options)
      if computer == "R":
        print("Computer chose Rock.")
        cRock = cRock + 1
      elif computer == "P":
        print("Computer chose Paper.")
        cPaper = cPaper + 1 
      elif computer == "S":
        cScissors = cScissors + 1
        print("Computer chose Scissors.")

      if player == computer:
        print ("Tie!")
        ties = ties + 1
      elif player == "R" and computer == "S":
        print ("You win!")
        wins = wins + 1
      elif player == "R" and computer == "P":
        print ("You lose!")
        losses = losses + 1
      elif player == "P" and computer == "R":
        print ("You win!")
        wins = wins + 1
      elif player == "P" and computer == "S":
        print ("You lose!")
        losses = losses + 1
      elif player == "S" and computer == "R":
        print ("You lose!")
        losses = losses + 1
      elif player == "S" and computer == "P":
        print ("You win!")
        wins = wins + 1
        
    

      if player == "R":   #our computer overlords keeping track of what a player is more likely to choose and making them miserable
        options.append("P")
        pRock = pRock + 1
      elif player == "P":
        options.append("S")
        pPaper = pPaper + 1
      elif player == "S":
        options.append("R")
        pScissors = pScissors + 1
    
    
  #Ask the user if they would like to play again.
    #User has option to stop playing in line 28, otherwise the game automatically repeats. I got annoyed having to enter Y or N everytime.

  #In the end, print the stats
  print("Final Stats:")
  print("Wins \t Ties \t Losses")
  print("---- \t ---- \t ------")
  print(wins, "\t", ties , "\t", losses)
  print(" ")
  print(" Player Choices:")
  print("Rock \t Paper \t Scissors")
  print("---- \t ---- \t ------")
  print(pRock, "\t", pPaper, "\t", pScissors)
  print(" ")
  print("Computer Choices:")
  print("Rock \t Paper \t Scissors")
  print("---- \t ---- \t ------")
  print(cRock, "\t", cPaper, "\t", cScissors)


if __name__ == '__main__':
  main()
