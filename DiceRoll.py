#DiceRoll.py
#Name: Grant Schaeffer
#Date: 10/4/25
#Assignment: Dice Roll
import random

def main():
  #Create an empty list with possible roll values
  rolls = [0,0,0,0,0,0,0,0,0,0,0,0]
  #Create two dice values ranging from 1 - 6 each
  for r in range(100):
    Dice1 = random.randint(1,6)
    Dice2 = random.randint(1,6)
    sum = 0
    sum = Dice1 + Dice2

  #find the sum total of the two dice
  rolls[sum - 1] = rolls[sum - 1] + 1
  print(rolls)
  #print statictics for dice rolls

  #for count in rolls:
    #dice = 1
    #print(dice, ": ", rolls)
    #dice = dice + 1

if __name__ == '__main__':
  main()
