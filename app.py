import base64
import json
import os

import pandas as pd
import requests

from flask import Flask, render_template
from GoogleNews import GoogleNews

app = Flask(__name__)

spreadsheet_id = os.environ["SPREADSHEET_ID"]
conteudo_codificado = os.environ["GOOGLE_SHEETS_CREDENTIALS"]
conteudo = base64.b64decode(conteudo_codificado)
credentials = json.loads(conteudo)
service_account = gspread.service_account_from_dict(credentials)
spreadsheet = service_account.open_by_key(spreadsheet_id) 
worksheet = spreadsheet.worksheet("Página1")

@app.route("/")
def hello_world():
    arquivo = open("templates/home.html")
    return arquivo.read()

@app.route("/nftnews")	
def nftnews():	
    googlenews=GoogleNews(period='d')	
    googlenews.setlang('pt')	
    googlenews.search('NFT')	
    result=googlenews.result()	
    df=pd.DataFrame(result)	
    del df['datetime']	
    worksheet.update([df.columns.values.tolist()] + df.values.tolist())
    return render_template open("templates/nftnews.html")
