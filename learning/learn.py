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

inventory = {
  'gold' : 500,
  'pouch' : ['flint', 'twine', 'gemstone'], # Assigned a new list to 'pouch' key
  'backpack' : ['xylophone','dagger', 'bedroll','bread loaf']
}

# Adding a key 'burlap bag' and assigning a list to it
inventory['burlap bag'] = ['apple', 'small ruby', 'three-toed sloth']

# Sorting the list found under the key 'pouch'
inventory['pouch'].sort()

# Your code here
inventory['pocket'] = ['seashell', 'strange berry', 'lint']
inventory['backpack'].sort()
inventory['backpack'].remove('dagger')
inventory['gold'] = inventory['gold'] + 50

#supermarket exercise practicing dictionaries and loops
prices = {
  "banana" : 4,
  "apple"  : 2,
  "orange" : 1.5,
  "pear"   : 3,
}
stock = {
  "banana" : 6,
  "apple"  : 0,
  "orange" : 32,
  "pear"   : 15,
}

for key in prices:
  print key
  print "price: %s" % prices[key]
  print "stock: %s" % stock[key]
print
print
total = 0
for key in prices:
  total += (prices[key] * stock[key])
print total

def compute_bill(food):
  total = 0
  for item in food:
    if stock[item] > 0:
      total += prices[item]
      stock[item] -= 1
  return total

#rock paper scissors exercise
"""
In this project, we'll build Rock-Paper-Scissors!
The program should do the following:
  1. Prompt the user to select either Rock, Paper, or Scissors.
  2. Instruct the computer to randomly select either Rock, Paper, or Scissors.
  3. Compare the user's choice and the computer's choice.
  4. Determine a winner (the user or the computer).
  5. Inform the user who the winner is.
"""
#import random integer function
from random import randint
#declare rock paper scissors list of options
options = ["ROCK", "PAPER", "SCISSORS"]
#dictionary that contains win/lose messages
message = {
  "tie": "Yawn it's a tie!",
  "won": "Yay you won!",
  "lost": "Aww you lost!"
}
#function that decides who the winner is
def decide_winner(user_choice, computer_choice):
  print "You chose %s" % user_choice
  print "The computer chose %s" % computer_choice
  if user_choice == computer_choice:
    print message["tie"]
  elif user_choice == options[0] and computer_choice == options[2]:
    print message["won"]
  elif user_choice == options[1] and computer_choice == options[0]:
    print message["won"]
  elif user_choice == options[2] and computer_choice == options[1]:
    print message["won"]
  else:
    print message["lost"]
#function that starts the game
def play_RPS():
  #determine user's selection/choice
  user_choice = raw_input("Enter Rock, Paper, or Scissors: ")
  #uppercase their input in case they enter lowercase
  user_choice.upper()
  #have computer make a random selection
  computer_choice = options[(randint(0, 2))]
  #call the decide_winner function passing in user's choice and the computer's choice
  decide_winner(user_choice, computer_choice)
#call the play_RPS function to start game
play_RPS()

#Teacher/Student Exercise with lists and dictionaries and functions
lloyd = {
  "name": "Lloyd",
  "homework": [90.0, 97.0, 75.0, 92.0],
  "quizzes": [88.0, 40.0, 94.0],
  "tests": [75.0, 90.0]
}
alice = {
  "name": "Alice",
  "homework": [100.0, 92.0, 98.0, 100.0],
  "quizzes": [82.0, 83.0, 91.0],
  "tests": [89.0, 97.0]
}
tyler = {
  "name": "Tyler",
  "homework": [0.0, 87.0, 75.0, 22.0],
  "quizzes": [0.0, 75.0, 78.0],
  "tests": [100.0, 100.0]
}

# Add your function below!
def average(numbers):
  total = sum(numbers)
  total = float(total)
  return total/len(numbers)

def get_average(student):
  homework = average(student["homework"])
  quizzes = average(student["quizzes"])
  tests = average(student["tests"])
  return 0.1 * homework + 0.3 * quizzes + 0.6 * tests

def get_letter_grade(score):
  if score >= 90:
    return "A"
  elif score >= 80:
    return "B"
  elif score >= 70:
    return "C"
  elif score >= 60:
    return "D"
  else:
    return "F"

def get_class_average(class_list):
  results = []
  for student in class_list:
    student_avg = get_average(student)
    results.append(student_avg)
  return average(results)
students = [alice, lloyd, tyler]
print get_class_average(students)
print get_letter_grade(get_class_average(students))

##########
#PYTHON 3
#########
def repeat_stuff(stuff, num_repeats = 10):
  return stuff*num_repeats
lyrics = repeat_stuff("Row ", 3) + "Your Boat. "
song = repeat_stuff(lyrics)
print(song)

train_mass = 22680
train_acceleration = 10
train_distance = 100

bomb_mass = 1
def f_to_c(f_temp):
  c_temp = (f_temp - 32) * 5/9
  return c_temp
f100_in_celsius = f_to_c(100)

def c_to_f(c_temp):
  f_temp = c_temp * (9/5) + 32
  return f_temp
c0_in_fahrenheit = c_to_f(0)

def get_force(mass, acceleration):
  return mass * acceleration
train_force = get_force(train_mass, train_acceleration)

print("The GE train supplies " + str(train_force) + " Newtons of force.")

def get_energy(mass, c = 3*10**8):
  return mass * c**2

bomb_energy = get_energy(bomb_mass)

print("A 1kg bomb supplies " + str(bomb_energy) + " Joules.")

def get_work(mass, acceleration, distance):
  return get_force(mass, acceleration) * distance

train_work = get_work(train_mass, train_acceleration, train_distance)

print("The GE train does " + str(train_work) + " Joules of work over " + str(train_distance) + " meters.")

#Try/Except statements
def raises_value_error():
    raise ValueError

try:
  raises_value_error()
except ValueError:
    print("You raised a ValueError!")

#Python 3 Sal's Shipping exercise
premium_ground_cost = 125
def ground_shipping(weight):
  cost = 0
  if weight <= 2:
    cost = weight * 1.50
  elif weight > 2 and weight <= 6:
    cost = weight * 3
  elif weight > 6 and weight <= 10:
    cost = weight * 4
  elif weight > 10:
    cost = weight * 4.75
  return float(cost) + 20
def drone_shipping(weight):
  cost = 0
  if weight <= 2:
    cost = weight * 4.50
  elif weight > 2 and weight <= 6:
    cost = weight * 9
  elif weight > 6 and weight <= 10:
    cost = weight * 12
  elif weight > 10:
    cost = weight * 14.25
  return float(cost)
def user_message(weight):
  #get cost from both functions based on weight
  ground_cost = ground_shipping(weight)
  drone_cost = drone_shipping(weight)
  #check which is the higher cost
  if ground_cost < drone_cost and ground_cost < premium_ground_cost:
    print("The cheapest method of shipping for your given weight is GROUND shipping")
    print("The cost of using this method of shipping is $" + str(float(ground_cost)))
  elif drone_cost < ground_cost and drone_cost < premium_ground_cost:
    print("The cheapest method of shipping for your given weight is DRONE shipping")
    print("The cost of using this method of shipping is $" + str(float(drone_cost)))
  elif premium_ground_cost < ground_cost and premium_ground_cost < drone_cost:
    print("The cheapest method of shipping for your given weight is PREMIUM GROUND shipping")
    print("The cost of using this method of shipping is $" + str(float(premium_ground_cost)) + "0")
  else:
    print("The program ran into an error")

user_message(4.8)
user_message(41.5)
