import os ##get the current paths so the db can be stored locally
from flask import Flask, render_template, request, flash, redirect, url_for, session
from flask_sqlalchemy import SQLAlchemy
app = Flask(__name__)
app.config['SECRET_KEY']='hgkjhkjhkjlhjkjk'

# setup SQLAlchemy
basedir = os.path.abspath(os.path.dirname(__file__))
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///' + os.path.join(basedir, 'data.sqlite')
db = SQLAlchemy(app)


# define database tables
class Artist(db.Model):
    __tablename__ = 'artists'
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(64))
    about = db.Column(db.Text)
    songs = db.relationship('Song', backref='artist', cascade="delete")##back reference at the many side, unue in ORM

class Song(db.Model):
    __tablename__ = 'songs'
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(256))
    year = db.Column(db.Integer)
    lyrics = db.Column(db.Text)
    artist_id = db.Column(db.Integer, db.ForeignKey('artists.id'))


@app.route('/')
def home():##view function, the name needs to be unique
    #return '<h1>hello world!!!!lllll</h1>'##codes have changed but the server hasn't been restarted
    return render_template('index.html')

@app.route('/artists')
def show_all_artists():
    artists = Artist.query.all()
    return render_template('artist-all.html', artists=artists)

@app.route('/user/<string:name>/')
def get_user(name):
    #return '<h1>hello %s your age is %d</h1>' % (name,3) ##codes have changed but the server hasn't been restarted
    return render_template('user.html', user_name=name)


@app.route('/songs')##every route needs a corresponding view function
def show_all_songs():
    songs=Song.query.all()
    return render_template('song-all.html', songs=songs)

@app.route('/artist/add', methods=['GET', 'POST'])
def add_artists():
    if request.method == 'GET':
        return render_template('artist-add.html')
    if request.method == 'POST':
        # get data from the form
        name = request.form['name']
        about = request.form['about']

        # insert the data into the database
        artist = Artist(name=name, about=about)
        db.session.add(artist)
        db.session.commit()
        return redirect(url_for('show_all_artists'))

@app.route('/artist/edit/<int:id>', methods=['GET', 'POST'])
def edit_artists(id):
    artist=Artist.query.filter_by(id=id).first()
    if request.method == 'GET':
        return render_template('artist-edit.html',artist=artist)
    if request.method == 'POST':
        # get data from the form
        artist.name = request.form['name']
        artist.about = request.form['about']

        db.session.commit()
        return redirect(url_for('show_all_artists'))

@app.route('/artist/delete/<int:id>', methods=['GET', 'POST'])
def delete_artists(id):
    artist=Artist.query.filter_by(id=id).first()
    if request.method == 'GET':
        return render_template('artist-delete.html',artist=artist)
    if request.method == 'POST':
        db.session.delete(artist)
        db.session.commit()
        return redirect(url_for('show_all_artists'))

@app.route('/song/add', methods=['GET', 'POST'])
def add_songs():
    artists=Artist.query.all()
    if request.method == 'GET':
        return render_template('song-add.html',artists=artists)
    if request.method == 'POST':
        # get data from the form
        name = request.form['name']
        year = request.form['year']
        lyrics = request.form['lyrics']
        artist_name = request.form['artist_name']
        artist= Artist.query.filter_by(name=artist_name).first()
        # insert the data into the database
        song = Song(name=name, year=year, lyrics=lyrics, artist=artist)
        db.session.add(song)
        db.session.commit()
        return redirect(url_for('show_all_songs'))

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
