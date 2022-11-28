
# Intrusion 

- For this one, running in virtual env due to dependency issues 
    -  `python -m venv env`
    -  `source env/bin/activate` 
    - to deactivate: `deactivate` 

## Brute Force Login 
- Main package: https://github.com/Sanix-Darker/Brute-Force-Login 
- Install: 
    - `git clone https://github.com/Sanix-Darker/Brute-Force-Login` 
    - `cd Brute-Force-Login`  
    - Needed to modify slighlyt, changing inside the /app folder, adding __init__.py and changing routes of modules 
    - Then run: `python main.py` or whatever depending on location (e.g., `python app/main.py`)
    - Then go through the options, and select the local running version of the PssP found in `Part8` folder - so the URL should be 0.0.0.0:80 and the two fields should be username and password 
    - Note - when running through these tests, check the output console in the running python program to see what it is actually doing 
    - Also show what happens when we change the file that loops through the passwords 

## Simple with WUZZ 
- Install: 
    - `git clone https://github.com/xmendez/wfuzz.git` 
    - `cd wfuzz` 
    - `pip install -r requirements.txt`
    - `wfuzz -h` 
    - `pip install wfuzz` 