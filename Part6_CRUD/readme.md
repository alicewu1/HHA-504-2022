# Run instructions 

- Since this version has the __main__, you can run this flask app using the pythong command: 
    - `sudo python app.py` 
- Or you can use python3 if that is what is found on your machine: 
    - `sudo python3 app.py` 
- The reason why we need `sudo` permissions here, is that if we are deploying our app on a remote server, to port :80, which is a special port (e.g., website traffic), we need to have elevated permissions

## ENV file structure: 
```
MYSQL_USERNAME = "SDF"
MYSQL_PASSWORD = "fSDFDF!"
MYSQL_HOST = "104.343.111.186"
```


- Other notes to organize: 
    - using the flask version of sqlalchemy https://flask-sqlalchemy.palletsprojects.com/en/3.0.x/quickstart/ 
    - declaring models https://flask-sqlalchemy.palletsprojects.com/en/3.0.x/models/
    - connecting to a MySQL database https://docs.sqlalchemy.org/en/14/dialects/mysql.html#module-sqlalchemy.dialects.mysql.mysqldb 

## Dependencies: 
- pip install flask flask-sqlalchemy PyMySQL 

## Future: 
- Signin: 
    - Azure AD ? 
    - GCP Firebase ? 
    - Build it ourselves? 

## Helpful tutorials: 
- Example 1: https://morioh.com/p/f38e3272d126 