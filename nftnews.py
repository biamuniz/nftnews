import base64
import json
import os

import pandas as pd
import requests

from GoogleNews import GoogleNews

spreadsheet_id = os.environ["GOOGLE_SHEET_ID"]
conteudo_codificado = os.environ["GOOGLE_SHEETS_CREDENTIALS"]
conteudo = base64.b64decode(conteudo_codificado)
credentials = json.loads(conteudo)
service_account = gspread.service_account_from_dict(credentials)
spreadsheet = service_account.open_by_key(spreadsheet_id) 
worksheet = spreadsheet.worksheet("Página1")

def nftnews():
    from GoogleNews import GoogleNews
    import pandas as pd
    googlenews=GoogleNews(period='d')
    googlenews.setlang('pt')
    googlenews.search('NFT')
    result=googlenews.result()
    df=pd.DataFrame(result)
    del df['datetime']
    worksheet.update([df.columns.values.tolist()] + df.values.tolist())
    return worksheet
