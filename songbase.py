from flask import Flask
app = Flask(__name__)

@app.route('/')
def home():
    return '<h1>hello world!!!!</h1>'##codes have changed but the server hasn't been restarted

@app.route('/user/<string:name>/')
def get_user(name):
    return '<h1>hello %s your age is %d</h1>' % (name,3) ##codes have changed but the server hasn't been restarted


if __name__ == '__main__':
   app.run(debug=True)##run it with a debug mode on
