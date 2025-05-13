import requests
import datetime
from urllib.parse import urlparse

def check_safe_browsing(url):
    # Replace with your actual Safe Browsing API key
    api_key = 'AIzaSyDa8QrFovPA9WUQ89ro1Xgzyx6xEtjHlmE'
    endpoint = f'https://safebrowsing.googleapis.com/v4/threatMatches:find?key={api_key}'
    body = {
        "client": {
            "clientId": "your-app",
            "clientVersion": "1.0"
        },
        "threatInfo": {
            "threatTypes": ["MALWARE", "SOCIAL_ENGINEERING"],
            "platformTypes": ["ANY_PLATFORM"],
            "threatEntryTypes": ["URL"],
            "threatEntries": [{"url": url}]
        }
    }

    response = requests.post(endpoint, json=body)
    if response.status_code == 200:
        return not bool(response.json().get("matches"))
    return True

def get_whois_data(url):
    try:
        domain = urlparse(url).netloc
        response = requests.get(f"https://api.whoisxmlapi.com/v1/whois?apiKey=YOUR_WHOIS_API_KEY&domainName={domain}")
        data = response.json()
        creation_date = data.get("WhoisRecord", {}).get("createdDate")
        if creation_date:
            creation = datetime.datetime.strptime(creation_date[:10], "%Y-%m-%d")
            age = (datetime.datetime.now() - creation).days
            return {'age_days': age}
    except:
        pass
    return None
