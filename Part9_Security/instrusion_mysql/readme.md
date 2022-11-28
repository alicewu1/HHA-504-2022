# SQLMAP 
- Library: https://github.com/sqlmapproject/sqlmap 
- Install: `git clone --depth 1 https://github.com/sqlmapproject/sqlmap.git sqlmap-dev` 
- Create venv - install requirements from txt file 
- Then to make sure working properly:
    - `python sqlmap.py -h` 
- For examples: 
    - https://github.com/sqlmapproject/sqlmap/wiki/Usage 

## Test endpoint with PaaS: 
- http://0.0.0.0/api/patients/acee0eea 

## Example test
- `python sqlmap.py -u "http://0.0.0.0/api/patients/acee0eea"` 
- Note - when running through these tests, check the output console in the running python program to see what it is actually doing 