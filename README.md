# python_toolbox
A collection of Python scripts and functions.

- Script: [environment_check.py](src/environment_check.py)

```bash
usage: environment_check.py [-h] [-d] requirement_file

Test whether all packages specified in the requirements.txt file are present in the current environment.

positional arguments:
  requirement_file  path to the requirement file

options:
  -h, --help        show this help message and exit
  -d, --debug       debug mode
```

```bash
$ python src/environment_check.py requirements.txt -d
Requirement: numpy>=1.18.5,<1.24.0          not satisfied!
Requirement: opencv-python>=4.1.1           not satisfied!
Requirement: ipython                        satisfied with ipython in python3.11/site-packages (from -r requirements.txt (line 34))
Requirement: psutil                         satisfied with psutil in python3.11/site-packages (from -r requirements.txt (line 35))
Some libraries are missing, you can try to run: pip install -U -r requirements.txt
```

- Function: [display_parameters](src/display_parameters.py)

Decorator to display function input parameters.

```python
@display_parameters
def a(v1, v2, v3=10, v4=18):
    pass

a(2, v2="t", v3=12)
```

```bash
*** Execution of: display_parameters.a(2, v2=t, v3=12)
```
