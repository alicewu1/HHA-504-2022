## What is gunicorn? 
- https://gunicorn.org/
- https://vsupalov.com/what-is-gunicorn/ 

## Notes: 
- If starting this on a new machine: 
    - `sudo apt-get update`
    - `sudo apt install python3-pip`
    - `sudo apt install gunicorn3` 
    - then install packages as normal: 
        - `pip install flask` 

- MAY need to add to path: `export PATH=$PATH:/usr/local/python3/bin` // should confirm

# to deploy: 
`sudo gunicorn3 -w 2 -b 0.0.0.0:80 app:app`  
