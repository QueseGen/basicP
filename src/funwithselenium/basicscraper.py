
from flask import Flask, render_template

from src.funwithselenium.actionclick import clickbutton

app=Flask(__name__)
app.config.from_pyfile('config.py') #Configure settings for Flask

@app.route("/selle")
def openhomepagewithChrome():

  return render_template("home.html")

if __name__ == '__main__':
  clickbutton()
  app.run()

 # time.sleep(15)
  #print("Click")




