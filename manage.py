from flask_script import Manager
from songbase import app, db, Artist, Song

manager=Manager(app)##create manager that manages the app created in songbase.py

# reset the database and create two artists
@manager.command
def deploy():
    db.drop_all()##make sure clean up all the DB
    db.create_all()##create DB new and any table if defined
    ##codes above are used to initialize the DB
    ##below is optional
    coldplay = Artist(name='Coldplay', about='Coldplay is a British rock band.')
    maroon5 = Artist(name='Maroon 5', about='Maroon 5 is an American pop rock band.')
    song1=Song(name='yellow', year=2004, lyrics='blah blah', artist=coldplay)##id is always automatically maintained
    song2=Song(name='yellow 2', year=2004, lyrics='blah blah', artist=coldplay)##id is always automatically maintained
    db.session.add(coldplay)
    db.session.add(maroon5)
    db.session.add(song1)
    db.session.add(song2)
    db.session.commit()##the 2 records are only added after you commit

if __name__ == '__main__':
    manager.run()
