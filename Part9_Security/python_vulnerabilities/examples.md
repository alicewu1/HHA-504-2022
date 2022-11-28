# Python Auditng 

## Pip Audit
- Audit dependencies for a requirements file, excluding system packages:
    - `pip-audit -r ./requirements.txt -l` 
- Audit dependencies for the current Python environment:
    - `pip-audit` 

## cve-bin-tool
- Install: 
    - `pip install cve-bin-tool[PDF]` 
    - `pip install --upgrade reportlab`
- Dependency: NVD API Key for faster updates 
    - Run: `cve-bin-tool -L requirements.txt --format console --nvd-api-key XKJHDFDKJSHD-FAKE-KEY-b269-920528256cf3`
- Then can do: 
    - `cve-bin-tool -L requirements.txt --format console `     #this provides a simple output in the console 
    - `cve-bin-tool -L requirements.txt --report -f html`          #this provides an output .html file 



