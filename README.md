

### Resources

- cygwin on Windows 10
- python 3 (installed via Cygwin installer)

### Features Used

- python 3
- SQLAlchemy
- Flask with JWT Authentication
- SQLite


### Installing Cygwin and Python3

- Re-run the cygwin install
- NOTE: if you haven't run Cygwin in a while, it upgrades lots/all packages
- Select mirror
- in the Package selector, select "Category" (much easier to read)
- Type "python3", and select the interpreter
- Type "pip3", and select the pip installer

### Installation

**Prep**

- Within Cygwin
- pip3 install virtualenv

**Creating virtualenv by hand (needs to be done once per installation)**
- virtualenv venv --python=python3
- python -V (will likely show you version 2)
- source venv/bin/activate
- python venv/bin/pip install -r requirements.txt

**Copy of requirements.txt**

```
aniso8601==2.0.0
click==6.7
Flask==0.12.2
Flask-JWT==0.3.2
Flask-RESTful==0.3.6
Flask-SQLAlchemy==2.3.2
itsdangerous==0.24
Jinja2==2.10
MarkupSafe==1.0
PyJWT==1.4.2
pytz==2017.3
six==1.11.0
SQLAlchemy==1.2.0
Werkzeug==0.14.1
```

installing the (slightly) harder way: python venv/bin/pip install Flask-RESTful Flask-JWT Flask-SQLAlchemy (also installs Flask)


**Starting the back-end server**
- source venv/bin/activate
- python app.py

**Running it**
- (within Cygwin) python3 app.py
- Should say:

```
* Running on http://127.0.0.1:5000/ (Press CTRL+C to quit)
```


### Other commands and notes

- python venv/bin/pip freeze
NOTE: you no longer need pip3
NOTE: turns out unix scripts cannot have a space in the shebang path, so "pip install Flask-RESTful" will fail 
