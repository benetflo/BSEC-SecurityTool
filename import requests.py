import requests
import re


def get_http_headers(url):
    
    try:

        if not re.match(r'http(s)?://[a-zA-Z0-9.-]+(?:/[a-zA-Z0-9._-]+)*', url):
            raise ValueError("Invalid URL. URL should start with http:// eller https://")

        response = requests.get(url, timeout=10) 
        response.raise_for_status()  # Kasta ett undantag om statuskod inte är 2xx
        return response.headers  # Header returned as dictionary
    
    except requests.exceptions.Timeout:
        print("\nERROR: Timeout - Servern svarade inte på förfrågan.")
        return None
    except requests.exceptions.RequestException as e:
        print(f"\nERROR: Ett problem inträffade vid förfrågan - {e}")
        return None
    except ValueError as e:
        print(f"\nERROR: {e}")
        return None
    

def print_info(headers):
    
    print("\nHTTP Headers Received:\n")
    if "date" in headers:
        print(f"HTTP-response received: {headers['date']}")
    if "server" in headers:
        print(f"Webserver/version: {headers['server']}")
    if "content-type" in headers:
        print(f"Content type: {headers['content-type']}")
    if "content-length" in headers:
        print(f"Content length in bytes: {headers['content-length']}")
    if "connection" in headers:
        print(f"TCP-connection: {headers['connection']}")
    if "access-control-allow-origin" in headers:
        print(f"Access-Control-Allow-Origin: {headers['access-control-allow-origin']}")
    if "access-control-allow-credentials" in headers:
        print(f"Access-Control-Allow-Credentials: {headers['access-control-allow-credentials']}")
    print()



while 1:
    try:
        url = input("B-HTTP-Header-Inspector$ ")
        if url.lower() == "exit":
            exit(0)
        else:
            headers = get_http_headers(url)
            headers = {key.lower(): value for key, value in headers.items()}
            if headers:
                print_info(headers)
            else:
                print("No headers to display.")
    except Exception as e:
        print(f"ERROR: {e}")

