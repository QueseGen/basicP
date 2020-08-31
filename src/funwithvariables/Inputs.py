# As important as 0's ans 1's are another fundamental of programming and computers is INPUT/OUTPUT
def Inputdemo():  # With the keyword input, we open a door for data to enter our program
  x = input("Type something\n")  # String type by default
  print(x, type(x))


def InputonlyIntsandfail():
  x = input("Enter a Whole Number\n")  # Now say want to build an calculator to add 2 numbers
  y = int(x)  # Parsing x won't work if someone enter anything other than a whole number
  print(y, type(y))


def InputonlyIntsuccessfully():
  try:
    x = input( "Enter a Whole Number\n")  # As you see, every input is a potential threat to your code so lets put safety nets
    y = int(x)
  except:
    x=input("Only Whole Numbers\n")
    y = int(x)  # Parsing x won't work if someone enter anything other than a whole number

# InputFlow()
InputonlyIntsuccessfully()

#I started here but regained my train of thought, started cleaning and rebuilding narrative

def InfinitySuccess():  # End Goal
  x = input("Enter a Whole Number\n")
  while type(x) != type(1):
    x = input("Only enter a whole Number\n")
  print("Thanks for entering ", x)

