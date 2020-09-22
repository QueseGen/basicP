import json
from flask import Flask, render_template
import requests
app=Flask("__name__", template_folder="templates")

@app.route("/load")
def jload():#CONSUME JSON
  w= '{"name":"JacQs)3", "age":26, "balance":1, "expectations":25000000000000}'  # JSON-will be a String Dictionary
  v= requests.get('https://api.github.com/events')
  x= json.loads(w)
  vv=v.json()
  print(str(x["name"])+"\n"+str(vv))
  return str(vv)

@app.route('/<name>/<int:age>/<int:balance>/<int:expectations>') #HTTPRequest to JSON to HTML
def home(name, age, balance, expectations):
  y={'Name': str(name), 'Age': age, 'Balance': balance, 'Expectations': expectations}
  z=str(y)
  return render_template('index.html', DC=y)

if __name__ == '__main__':
  jload()
  app.run()