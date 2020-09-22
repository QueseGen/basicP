
def openfiles(filename="wordcount"):  #When setting function params try setting default values
  f=open(filename,"r")      #Open File
  data=f.read()             #Read data
  newdata=data.split(":>")  #Manipulate   |split can be called on a string to break into an array by seperator
  print(data,"\n", newdata,"\n", type(newdata), "\n", len(newdata))
  f.close()                 #Close File


def openfilesgettwo(filename="wordcount"):  #When setting function params try setting default values
  f=open(filename,"r")      #Open File
  data=f.read()             #Read data
  newdata=data.split(":>")  #Manipulate   |split can be called on a string to break into an array by seperator
  f.close()  # Close File
  return data,newdata

def writefile(filename="wordcount"):
  f=open(filename,"r+w")
  pass

if __name__ == '__main__':
    #openfiles()
    data,ndata=openfilesgettwo()
    print(data, "\n", ndata, "\n", type(ndata), "\n", len(ndata))
