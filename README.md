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

### Coverage Test
```
# RUN
coverage run -m unittest discover -s tests 
  # discover: will search for test*.py files  
  # -s: directoery of testing scripts  

#Print result
coverage report -m

# Html result
coverage html -d coverage_html
```

### Formatter
- flake8
- black

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