from flask import Flask

app = Flask(__name__)

@app.route('/hello')

def hello_route():
    print("Hello World, we are learing Flask")
    return "Hello"
  
app.run()