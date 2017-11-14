from flask import Flask, render_template, request, flash, redirect, url_for, session
app = Flask(__name__)
app.config['SECRET_KEY']='hgkjhkjhkjlhjkjk'

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

@app.route('/form-demo', methods=['GET','POST'])
def form_demo():##view function, the name needs to be unique
    if request.method=='GET':
        first_name=request.args.get('first_name')
        if first_name:
            return render_template('form-demo.html',first_name=first_name)
        else:
           first_name=session.get('first_name')
           return render_template('form-demo.html',first_name=first_name)
    if request.method=='POST':
        session['first_name']=request.form['first_name']
        return redirect(url_for('form_demo'))
