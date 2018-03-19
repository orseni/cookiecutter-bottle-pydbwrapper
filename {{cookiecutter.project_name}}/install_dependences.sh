pip install --upgrade pip
for req in $(cat requirements.txt); do pip install -U $req; done
pip install -U git+https://github.com/orseni/pydbwrapper