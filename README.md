# python_project
A basic project setup for python.


## Package management
- pip  
  Packagemanagement
- venv  
  Virtual environment
- pip-chill  
  Simplified dependency list, it ignores the dependent packages.

# Python

### mypy CLI
mypy only support python above version 3.4  
It will by default search config file called `mypy.ini` or `*.mypy.ini` under current working directory.
```
mypy --python-version <X.Y> --ignore-missing-imports [filename or directory]

# mypy --python-version 3.4 --ignore-missing-imports file1 file2 dir1
```
### Coverage Test CLI
It will by default search config file called `.coveragerc` under current working directory.
```
# RUN
coverage run -m unittest discover -s tests 
  # discover: will search for test*.py files  
  # -s: directoery of testing scripts  

# Print result
coverage report -m

# Html result
coverage html -d coverage_html
```

### Formatter: Black CLI
```
black <filename or directory>
```  
For vscode, you could install extension `emeraldwalk.runonsave` to format your scripts on save.

# Jupyter notebook

### Sync notbook with python script
This only works with jupyter-lab and it requires some setup for the ipynb file.
- jupytext  
[paired notebook](https://jupytext.readthedocs.io/en/latest/paired-notebooks.html)
[how-to-version-control-jupyter](https://nextjournal.com/schmudde/how-to-version-control-jupyter)

### Formatter
- black
```python
jupyter nbextension install https://github.com/drillan/jupyter-black/archive/master.zip -- user
jupyter nbextension enable jupyter-black-master/jupyter-black
```