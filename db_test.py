# db_test.py
from http.server import BaseHTTPRequestHandler
import pandas as pd
import requests
from urllib import parse
import psycopg2
import json
from sqlalchemy import create_engine
import plotly.express as px
import plotly.graph_objects as go
from dash import Dash, dcc, html, Input, Output
import dash_bootstrap_components as dbc
import os

POSTGRES_URL = "postgresql+psycopg2://default:RmnVj6YBICZ1@ep-little-field-a2wcjsug.eu-central-1.aws.neon.tech:5432/verceldb?sslmode=require"
POSTGRES_USER = "default"
POSTGRES_HOST = "ep-little-field-a2wcjsug-pooler.eu-central-1.aws.neon.tech"
POSTGRES_PASSWORD = "RmnVj6YBICZ1"
POSTGRES_DATABASE = "verceldb"

engine = create_engine(POSTGRES_URL)


def fetch_data_with_pagination(url, payload):
    all_data = []
    page = 1
    while True:
        payload['page'] = page
        response = requests.post(url, json=payload)
        if response.status_code == 200:
            data = response.json()
            if not data['data']:
                break
            all_data.extend(data['data'])
            page += 1
        else:
            print("Failed to retrieve data. Status code:", response.status_code)
            return None
    return all_data


url_quotes = "https://syzygy.scoro.com/api/v2/quotes/list"
api_key = "ScoroAPI_b10a196258691bb" 
company_account_id = "syzygy"
payload_quotes = {
    "lang": "eng",
    "apiKey": api_key,
    "company_account_id": company_account_id,
    "request": {},
    "filter": {}
}
quotes = fetch_data_with_pagination(url_quotes, payload_quotes)
if quotes:
    df_quotes = pd.DataFrame(quotes)
    df_quotes.to_sql('quotes', engine, if_exists='replace', index=False)
