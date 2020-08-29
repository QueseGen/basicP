

# PEEL BACK ONE LESSON AT A TIME | remove # before the prints after understanding of prior message
def calculateint():
  #value to the right will be assigned name to the left, this is called variables and values
  x=5  #x is a variable that holds the value of integer 5
  y=4  #with python you dont have to specify type
  z=x+y #With Integers we can do the full range of operators: +,-,*,/,%
  print(z)

def calculateintmaybe():
  x=5
  y=int("4")  #numbers are simple but there are more data types like strings, here we use int() to convert a string to an integer
  z=x+y   # if y equaled "4" we will not be able to add because "" represents strings or words
  print(z) #it works because now 5+"4" becomes 5+4

def calculatestrings():
  x="5" #Okay earlier we touched on strings, now lets add them | WE CAN ONLY ADD STRINGS
  y="4"
  z=x+y #Guess the answer
  print(z)
  z=z+str(5) #Now, when adding values they MUST be of  the same type in Python
  #print(z)   #Additionally you may have notice we took the original z and added "5" to make a new z | change the value

def calculatetheTruth(): #Now, that we went over simple whole numbers(integers) and characters(strings) lets evaluate using booleans
  y = 5 > 4  #Boolean is the simpliest and most important code of life: True(1) or False(0) |
  print(y) #We give the varable a statement and it will evaluate whether it is truth or false
  x=5<4
  #print(x) #guess this one, 5 is less than 4

  #There are more operators such as == for equals, || for or , && for and, =< for equal or less than,=> for equal or greater than
  z= x or y #I goofed. In Python: or for or, and for and, != or not for not
  #print(z)
  #print(x==0) #Like mentioned on line 24 Boolean is the simpliest and most important code of life: True(1) or False(0) | value of x equaled False or 0, so statement printed is true

if __name__ == '__main__':
  calculateint()
  #calculateintmaybe()
  #calculatestrings() #Maybe not what you expect but you have to remember these are no longer numbers..they are characters/words
  #calculatetheTruth() #One True make a true but two wrongs dont make a right :>