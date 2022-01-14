import base64
import json
import os

import pandas as pd
import requests

from flask import Flask, render_template
from GoogleNews import GoogleNews

app = Flask(__name__)


@app.route("/")
def hello_world():
    arquivo = open("templates/home.html")
    return arquivo.read()

@app.route("/nftnews")	
def nftnews():	
    arquivo = open("templates/nftnews.html")
    return arquivo.read()
