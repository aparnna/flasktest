from flask import Flask
from flask import redirect
from flask.ext.script import Manager
app = Flask(__name__)
manager = Manager(app)

@app.route('/')
def index():
    return '<h1>Hello World!</h1>'

@app.route('/abc')
def abc():
    return '<h2>abc - sample prgm</h2>'

@app.route('/add/<x>/<y>')
def add(x,y):
    res = int(x)+int(y)
    return '<h2>%s</h2>' % res, 404
    
@app.route('/user/<name>')
def user(name):
    if name == "google":
      return redirect("http://www.google.com")
    else:
      return '<h2> hello %s</h2>' %name
    
if __name__ == '__main__':
    #app.run(debug=True)
    manager.run()
