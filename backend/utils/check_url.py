import tldextract
import re
from utils.api_helpers import get_whois_data, check_safe_browsing

def analyze_url(url):
    result = {
        'url': url,
        'suspicious': False,
        'reason': [],
    }

    # Check for HTTP
    if not url.startswith('https'):
        result['suspicious'] = True
        result['reason'].append('Not using HTTPS')

    # Check for too many dots or hyphens
    if url.count('.') > 3 or '-' in url:
        result['suspicious'] = True
        result['reason'].append('Unusual domain pattern')

    # Check Safe Browsing
    if not check_safe_browsing(url):
        result['suspicious'] = True
        result['reason'].append('Blacklisted by Google Safe Browsing')

    # WHOIS check
    whois_info = get_whois_data(url)
    if whois_info and whois_info.get('age_days', 9999) < 30:
        result['suspicious'] = True
        result['reason'].append('Recently registered domain')

    return result
