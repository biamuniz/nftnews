import base64
import datetime
import json
import os
nome = "XXXXX"
spreadsheet_id = "SPREADSHEET_ID"

arquivo = open(nome)
credentials = json.load(arquivo)
service_account = gspread.service_account_from_dict(credentials)
spreadsheet = service_account.open_by_key(spreadsheet_id)
worksheet = spreadsheet.worksheet("Página1")
