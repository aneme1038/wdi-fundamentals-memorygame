print("this is a message of my choosing")
points = 5
exercises = 5.1
total = points + float(exercises)
print(total)

"""
This program should do the following:
1. Prompt the user to select a shape.
2. Calculate the area of that shape.
3. Print the area of that shape to the user.
"""
print "Area Calculator"
option = raw_input("Enter C for Circle or T for Triangle: ")
if option == 'C':
  radius = float(raw_input("Enter the radius for your circle: "))
  area = 3.14159 * radius**2
  print "The area of your circle with a radius of %s is %s" % (radius, area)
elif option == 'T':
  base = float(raw_input("Enter a base length for your triangle: "))
  height = float(raw_input("Enter the height of your triangle: "))
  area = 0.5 * base * height
  print "The area of your triangle with a base of %s and a height of %s is %s" % (base, height,     area)
else:
  print "You entered an invalid shape/entry!"
print "Program is now exiting"

"""
This program should do the following:
1. Roll a pair of dice.
2. Add the values of the roll.
3. Ask the user to guess a number.
4. Compare the user's guess to the total value.
5. Determine the winner (user or computer)
"""

from random import randint
from time import sleep

def get_user_guess():
  guess = int(raw_input("Guess a number between 2 and 12"))
  return guess
def roll_dice(number_of_sides):
  first_roll = randint(1, number_of_sides)
  second_roll = randint(1, number_of_sides)
  max_val = number_of_sides * 2
  print "The maximum value of the dice is %d" % (max_val)
  guess = get_user_guess()
  if guess > max_val:
    print "What you entered is invalid."
  else:
    print "Rolling..."
    sleep(2)
    print "The first rolled dice shows a %d" % (first_roll)
    sleep(1)
    print "The second rolled dice shows a %d" % (second_roll)
    sleep(1)
    total_roll = first_roll + second_roll
    print total_roll
    print "Result..."
    sleep(1)
    if guess == total_roll:
      print "You won! You guessed the roll!"
    else:
      print "You lost! Game Over! Try Again!"

roll_dice(6)
