#Here I will cover:
#Variables and Values
#Basic Data Types
#Conversion/Parsing
#Addition

# PEEL BACK ONE LESSON AT A TIME | remove # before the prints after understanding of prior message
def keepitSimple(): #Variables and Values: In programming we make our own logic.
  one=1             #We can name(declare) variables and give(assign) them a value..
  two=2             #In Python you don't have to specify type, whatever is right will be saved to left in same form.
  print(one+two)    #Prints 3

  one=2             #Values can be changed, per request..
  print(one+two) #Guess

def calculateIntegers(): #Integers/int(): Whole Numbers are called Integers...1,2,3,4,5,etc and their negative counterparts.
  x,y=5,4           #We can also declare and assign two variables at the same time..

  z=x+y             #In Math these are called Operators: +(add),-(subtract),*(multiple),/(divide),%(module,for later....)
  print(z)

def calculateStrings(): #Strings/str(): Numbers are simple but there are more types of Data like Strings,
  x="5"                 #Strings are like spoken words.
  y="4"
  z=x+y #Guess
  print(z)


def calculatetheRightway(): #Conversion: Now, when adding values in Python they MUST be of the same type.
  x=5
  y=int("4")        #Here we use int()| to convert a string("4") to an Integer(4)
  z=x+y
  print(z)          #Now 5+"4" becomes 5+4

  z=str(z)+str(x)   #All Variables are resusable(unless constant) and assigment of values start from right to left.
  print(z) #Guess


def calculatetheTruth(): #Booleans/bool(): Now, that we went over simple whole Numbers(Integers) and Spoken Words(Strings)..

  #Boolean is the simpliest datatype: True equals 1 and  False equals 0
  x = 5 > 4         #A statement can either be True or False.
  print(x) #Is 5 greater than 4 ?
  y=5<4
  print(y) #Guess

  #Python makes statements more readable: or/not/and/</>/==/<=/>=
  x, y = True, False #True represents 1 and False represents 0, all things are made of 0's and 1's.
  z= x or y
  print(z)           #True or False will always be True however, True and False cannot exist at once.
  print(y==0) #Does left value equal right value?

def calculateFloats(): #Floats/float(): are Numbers with decimals float()|
    x=1.4
    print(type(x)) #Python has many neat shortcuts.. type| shows what data type of specified variable
    y=2
    print(x+y)     #Floats are the dominant number type
    print(1/2) #Thankfully Python converts Integers to Floats at runtime, other languages don't

if __name__ == '__main__':
  calculateIntegers()

  line=6
  dic=list(range(line+1)[1::])  #Data Structure: Dictonary
  tup=("This is a Tuple: ", list(range(line + 1)))     #Data Structure: Tuple

  print(tup[0]+str(tup[1]) )#This is a Tuple: [0, 1, 2, 3, 4, 5, 6]

  print(dic,tup)     #print values
  print(dic, tup)   #print a tuple
  #calculatetheRightway()
  #calculateStrings()
  #calculatetheTruth() #Two wrongs dont make a right
  #calculateFloats()

#Next Subject: Flows.py , list/tuples/dictionaries will all come in due time.