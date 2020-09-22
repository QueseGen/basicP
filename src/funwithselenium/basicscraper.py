import time
from selenium import webdriver
from flask import Flask, render_template

app=Flask(__name__)

def clickbutton():
    driver = webdriver.Chrome(executable_path="./driver/chromedriver.exe")
    driver.get("http://127.0.0.1:5000/selle")
    driver.implicitly_wait(10)
    time.sleep(5)
    button=driver.find_element_by_id("butt")
    button.click()
    driver.quit()

@app.route("/selle")
def openhomepagewithChrome():
  return render_template("home.html")

if __name__ == '__main__':
  clickbutton()
  app.run()
