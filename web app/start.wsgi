import sys, os
import logging

activate_this = os.path.join(os.path.dirname(__file__), 'venv/bin', 'activate_this.py')
execfile(activate_this, dict(__file__=activate_this))

# To include the application's path in the Python search path
logging.basicConfig(stream=sys.stderr)
sys.path.insert(0, os.path.dirname(__file__))
print("### WSGI PATH LOADING ###")
print(sys.path)

from app import app as application