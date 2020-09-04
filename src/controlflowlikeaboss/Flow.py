#Lets make Flows f


def Infinity(): #To Infinity and beyond
  while True:  #while| is a very powerful keyword...it makes whatever is in scope run over and over again in a loop
    print("Yoo")
    break #break| breaks the cycle and/or the current scope that it is in so code can keep moving

def ifElse(): #Control through Evaluation
   x, y = 5, 4
   if x >y: #The if| keyword evaluates the primary statement then executes if true.
     print(x, " is greater than ", y)
   else:    #If the if| statement is false the only option would be else| so doesn't need statement
     print(y, " is greater than ", x)

#Additionally, we have elif|,else-if that evaluate other statements chronologically...
#only if none are true the else| will execute.
#Based on values, guess which statement executes
   x, y, z = 2, 3, 5
   if x==3:
     print("Should never happen, x equals ", x)
   elif y==2:
     print("Should never happen, y equals ", y)
   elif z==(x+y):
     print("The sum of x and y are equal is ", z)
   else:
     print("I give up.")

def movingon():
  x,y=0,True  #Lets declare two variables| at once using a comma
  while y:  #Now we have the making of an infinite loop
    print(x,"Yo")
    x+=1 #AKA x=x+1 | Let's add 1 to x everytime we loop
    if x>5: #And turn loop off when x is greater than 5 by making y=False
      y=False

def letsexpand():
    pass #Will pickup with

Infinity() #If you remove the break| "Yoo" would be printed infinitely, NEVER WISE ALWAYS STOP YOUR PROGRAMS WHEN NOT IN USE.
ifElse()
movingon() #Remember, most programs always run until a specific condition is met...there is a loop and a trigger