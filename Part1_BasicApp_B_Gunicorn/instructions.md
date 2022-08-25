### New Requirements: 
`pip3 install Flask gunicorn`

## What is gunicorn? 
- https://gunicorn.org/
- https://vsupalov.com/what-is-gunicorn/ 

## Notes: 
- Have now removed the __main__ part of the flask app, gunicorn takes over 
- Might though need to add it back in 

# to deploy: 
`gunicorn -w 2 -b 0.0.0.0:80 app.py:app`  
