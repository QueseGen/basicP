
def modifyString():
   x="strinG"
   print(len(x))     #Counts how many letters are in string | 6
   y=x.capitalize()  #Caps first letter  | "StrinG"
   y=x.upper()       #Caps all letters   | "STRING"
   y=x.lower()       #Lowercase all letters | "string"
   y=x.replace("i","o") #replace changes a letter found in string to another
   v="Be gone thot."
   z=v.replace(" ","") # Remove spaces from string
   print(y+"\n",z,)

   #You can always browser the full catelog of mods/methods by adding a . after the variable
   pass #Is a way of ending scope of a method

if __name__ == '__main__':
      modifyString()