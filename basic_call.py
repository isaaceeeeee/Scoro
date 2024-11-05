# Basic API Call
import pandas as pd
import requests
import json

# Import the data with pagination to bypass the maximum request limit
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

# Simple API Request
url = "https://{company_site}/api/v2/quotes/list" # Replace {company_site} with your own site 
api_key = "API_KEY" 
company_account_id = "ACCOUNT_ID"
payload = {
    "lang": "eng",
    "apiKey": api_key,
    "company_account_id": company_account_id,
    "request": {},
    "filter": {},
    "detailed_response": True,
}
df = fetch_data_with_pagination(url, payload)
if df:
    print(json.dumps(df, indent=4))
    df = pd.DataFrame(df)
