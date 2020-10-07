import os
import time
import tkinter
from tkinter import messagebox

from flask import Flask
from selenium import webdriver

parent = tkinter.Tk() # Create the object
parent.overrideredirect(1) # Avoid it appearing and then disappearing quickly
parent.iconbitmap("PythonIcon.ico") # Set an icon (this is optional - must be in a .ico format)
parent.withdraw() # Hide the window as we do not want to see this one
app=Flask(__name__)
app.config.from_pyfile('config.py') #Configure settings for Flask

#Loads Chrome
def chroming():
  PROJECT_ROOT = os.path.abspath(os.path.dirname(__file__))
  DRIVER_BIN = os.path.join(PROJECT_ROOT, "/Applications/chromedriver")
  return webdriver.Chrome(executable_path=DRIVER_BIN)



def clickbutton(): #Learning more on concurrency and parrelelism to run local app and web app concurrently
  PROJECT_ROOT = os.path.abspath(os.path.dirname(__file__))
  DRIVER_BIN = os.path.join(PROJECT_ROOT, "/Applications/chromedriver")
  driver = webdriver.Chrome(executable_path=DRIVER_BIN)
  driver.get("http://127.0.0.1:5000/selle")
  #button = driver.find_element_by_id("butt")
  #button.click()

  driver.quit()


def searchgoogle(topic):
  driver = chroming()
  driver.get("https://duckduckgo.com")
  search = driver.find_element_by_name("q") #Inspect web pages to find the object you would like to select
  search.clear() #clear current value
  search.send_keys(topic) #send new value
  search.submit()
  time.sleep(5)
  results=driver.find_element_by_id("links")
  print(results.get_property())
  for result in results:
    print(result)
  driver.close()
  #gselect=driver.find_element_by_name("")


def searchtime(destination, count):

  if destination.lower().endswith(".com"):
    driver=chroming()
    driver.get("https://"+destination)
    time.sleep(count)
    yesno = messagebox.askyesno('Question Title', 'Are you sure you want to undo?', parent=parent)
    #popup asking if would like to continue

    driver.quit()
  elif destination.lower().endswith("do",0,1):
    print("Lets do it!!!")
    time.sleep(count)
  else:
    print("Ok")
    time.sleep(count)





if __name__ == '__main__':
  #searchgoogle("Ducks")
  searchtime(input("Where are we going?\n"), int(input("How long are you visiting?\n")))

