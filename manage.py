from flask_script import Manager
from songbase import app


manager=Manager(app)##create manager that manages the app created in songbase.py


if __name__ == '__main__':
    manager.run()
