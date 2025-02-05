#TempConvert.py
#Name:
#Date:
#Assignment:


def main():
  #Prompt the user for a Fahrenheit temperature
  fTemp = input ("Input a temperature in degrees Fahrenheit: ")

  #Convert that temperature to celsius, rounding to 1 decimal percision
  cTemp = (float(fTemp) - 32) * (5/9)
  cTempRound = round (cTemp, 1)

  #Output converted temperature.
  

  print(fTemp, "degrees Fahrenheit is", cTempRound, "degrees Celsius.")
if __name__ == '__main__':
  main()
