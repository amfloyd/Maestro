from flask import Flask, abort, jsonify, request, render_template
from sklearn.externals import joblib
import numpy as np
import json
app = Flask(__name__)

@app.route('/')
def home():
    return render_template('index.html')