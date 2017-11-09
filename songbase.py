from flask import Flask, render_template
app = Flask(__name__)

@app.route('/')
def home():##view function, the name needs to be unique
    #return '<h1>hello world!!!!lllll</h1>'##codes have changed but the server hasn't been restarted
    return render_template('index.html')

@app.route('/user/<string:name>/')
def get_user(name):
    #return '<h1>hello %s your age is %d</h1>' % (name,3) ##codes have changed but the server hasn't been restarted
    return render_template('user.html', user_name=name)


@app.route('/songs')##every route needs a corresponding view function
def get_all_songs():
    songs=[
    'song 1',
    'song 2',
    'song 3'
    ]
    return render_template('songs.html', songs=songs)


if __name__ == '__main__':
   app.run()##run it with a debug mode on
