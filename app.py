import csv
import io
import requests
from flask import Flask
import pandas as pd
from GoogleNews import GoogleNews
import pandas as pd

app = Flask(__name__)

@app.route("/")
def hello_world():
    arquivo = open("templates/home.html")
    return arquivo.read()

@app.route("/sobre")
def sobre():
    arquivo = open("templates/sobre.html")
    return arquivo.read()

@app.route("/nftnews")
def tweetify():
    arquivo = open("templates/nftnews.html")
    return arquivo.read()


def nftnews():
    googlenews=GoogleNews(period='d')
    googlenews.setlang('pt')
    googlenews.search('NFT')
    result=googlenews.result()
    df=pd.DataFrame(result)
    del df['datetime']
    worksheet.update([df.columns.values.tolist()] + df.values.tolist())
    return df
