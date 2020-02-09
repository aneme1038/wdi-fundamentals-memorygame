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
