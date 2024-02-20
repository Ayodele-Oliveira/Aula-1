#EXERCISE: implement the above switch case example using if/else conditions
#Prompt: For each digit between 0-9, the program will print a confirmation 
#for the entered value or print "invalid inputs" for all other numbers.

number = input("Insert a number, please")
if (number == '0'):
  print("Entered 0 ")
elif (number == '1'):
  print("Entered 1")
elif (number == '2'):
  print("Entered 3")
elif (number == '4'):
  print("Entered 4")
elif (number == '5'):
  print("Entered 5")
elif (number == '6'):
  print("Entered 6")
elif (number == '7'):
  print("Entered 7")
elif (number == '8'):
  print("Entered 8")
elif (number == '9'):
  print("Entered 9")
else:
  print("Invalid Inputs")