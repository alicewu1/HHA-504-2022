### Step 1
`python3 -m venv ~/.venvs/flask`

### Step 2
`source ~/.venvs/flask/bin/activate`

### Step 3
`pip3 install Flask gunicorn`

### Step 4
`pip freeze > requirements.txt`

### Step 5
- Insert into a gunicorn_config.py file:
```
bind = "0.0.0.0:8080"
workers = 2
```

### Step 7
- Local run: 
`export FLASK_APP=app.py` 
`sudo -E bash -c 'echo $FLASK_APP'` 
- Local run command with default: 
`flask run` 
- Local run command wiht arguments:  
`flask run -h localhost -p 3000` 
`sudo flask run -h localhost -p 80`

### Step 8 
- Run command for web:
`sudo python app.py` 