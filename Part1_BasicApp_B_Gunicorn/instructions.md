## What is gunicorn? 
- https://gunicorn.org/
- https://vsupalov.com/what-is-gunicorn/ 

## Notes: 
- `sudo apt install gunicorn3`
- See if need to add to path: `export PATH=$PATH:/usr/local/python3/bin` 

# to deploy: 
`sudo gunicorn3 -w 2 -b 0.0.0.0:80 app:app`  
