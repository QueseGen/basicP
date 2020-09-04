
def openfiles(filename="wordcount"):
  f=open(filename,"r")
  data=f.read()
  print(data)

if __name__ == '__main__':
    openfiles()