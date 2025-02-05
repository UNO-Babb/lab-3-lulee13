#ApproxPi.py
#Name:
#Date:
#Assignment:
import math
import time


#PLEASE NOTE - This is an optional, extra credit portion of the lab.

def main():
  realPi = math.pi

  #ask user for decimal percision (up to 10)
  precision = input("How many decimal places would you like? ")
  
  start = time.time()
  #calculate pi using the approximation technique
  


  #Loop until the level of percision is reached

  end = time.time()

  elapsedTime = end - start
  print(elapsedTime)

if __name__ == '__main__':
  main()
