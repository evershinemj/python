- download **pip tar ball** with `wget`, `curl` or from `pypi`.
- unzip the tar ball with `tar -zxvf <tar-file>`.
- `cd` the extracted directory.
- run `python setup.py install`.
---
note that **setup.py** is in the working directory(hence also in PYTHONPATH/sys.path, as '.' is included in PYTHONPATH/sys.path).
---
note that `pip.exe` is installed under a ==newly created directory== **Scripts**, which is under **PYTHON_HOME**.
---
note that **Scripts** is automatically added to $PATH.
