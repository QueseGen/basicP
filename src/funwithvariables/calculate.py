
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

if __name__ == '__main__':
  #calculateint()
  calculateintmaybe()