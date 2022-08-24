### Step 1
`python3 -m venv ~/.venvs/flask`

### Step 2
`source ~/.venvs/flask/bin/activate`

### Step 3
`pip3 install Flask`
<!-- `pip install Flask gunicorn` -->

### Step 4
`pip freeze > requirements.txt`

### Step 5
- Insert into a app.py file: 
```
from flask import Flask
app = Flask(__name__)

@app.route('/')
def hello_world():
    return 'Hello Sammy!'
```

### Step 6
- Local run: 
`export FLASK_APP=app.py` 
`sudo -E bash -c 'echo $FLASK_APP'` 
- Local run command with default: 
`flask run` 
- Local run command wiht arguments:  
`flask run -h localhost -p 3000` 
`sudo flask run -h localhost -p 80`

