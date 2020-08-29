
def calculateint():
  #value to the right will be assigned name to the left, this is called variables and values
  x=5  #x is a variable that holds the value of integer 5
  y=4  #with python you dont have to specify type
  z=x+y
  print(z)

def calculateintmaybe():
  x=5
  y=int("4")  #numbers are simple but there are more data types like strings, here we use int() to convert a string to an integer
  z=x+y   # if y equaled "4" we will not be able to add because "" represents strings or words
  print(z) #it works because now 5+"4" becomes 5+4

def calculatestrings():
  x="5" #Okay earlier we touched on strings, now lets add them
  y="4"
  z=x+y #Guess the answer
  print(z)
  z=z+str(5) #Now, when adding values they MUST be of  the same type in Python
  print(z)   #Additionally you may have notice we took the original z and added "5" to make a new z | change the value


if __name__ == '__main__':
  #calculateint()
  #calculateintmaybe()
  calculatestrings() #Maybe not what you expect but you have to remember these are no longer numbers..they are characters/words