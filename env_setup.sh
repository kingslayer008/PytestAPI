export PYTHON_VENV=venv
rm -rf $PYTHON_VENV
python3 -m pip install virtualenv
python3 -m pip install -U pip
python3 -m pip install -U virtualenv
python3 -m virtualenv $PYTHON_VENV
source $PYTHON_VENV\bin\activate
python3 -m pip install --progress-bar on --requirement requirements.txt
