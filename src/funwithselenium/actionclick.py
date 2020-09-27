import os
import time
from selenium import webdriver

def clickbutton(): #Learning more on concurrency and parrelelism to run local app and web app concurrently
  PROJECT_ROOT = os.path.abspath(os.path.dirname(__file__))
  DRIVER_BIN = os.path.join(PROJECT_ROOT, "/Applications/chromedriver")
  driver = webdriver.Chrome(executable_path=DRIVER_BIN)
  driver.get("http://127.0.0.1:5000/selle")
  #button = driver.find_element_by_id("butt")
  #button.click()
  driver.quit()

def googler():
  PROJECT_ROOT = os.path.abspath(os.path.dirname(__file__))
  DRIVER_BIN = os.path.join(PROJECT_ROOT, "/Applications/chromedriver")
  driver = webdriver.Chrome(executable_path=DRIVER_BIN)
  driver.get("https:google.com")
  gsearch = driver.find_element_by_name("q") #Inspect web pages to find the object you would like to select
  gsearch.clear() #clear current value
  gsearch.send_keys("Wawa near me") #send new value
  gsearch.submit()
  driver.quit()

googler()