import requests
import re

# Function to get HTTP headers from a URL
def get_http_headers(url):
    try:
        # Validate the URL to ensure it starts with http:// or https://
        if not re.match(r'http(s)?://[a-zA-Z0-9.-]+(?:/[a-zA-Z0-9._-]+)*', url):
            raise ValueError("Invalid URL. URL should start with http:// or https://")

        # Send an HTTP GET request with a timeout of 10 seconds
        response = requests.get(url, timeout=10)

        # Raise an exception if the response status code is not 2xx (successful)
        response.raise_for_status()
        
        # Return the HTTP headers as a dictionary
        return response.headers

    except requests.exceptions.Timeout:
        # If the request times out (server didn't respond in time)
        print("\nERROR: Timeout - The server didn't respond to the request.")
        return None
    except requests.exceptions.RequestException as e:
        # General exception if there's an error in the request (e.g., network issues, invalid response)
        print(f"\nERROR: A problem occurred during the request - {e}")
        return None
    except ValueError as e:
        # If the URL is invalid (doesn't start with http:// or https://)
        print(f"\nERROR: {e}")
        return None

# Function to print out HTTP headers in a readable format
def print_info(headers):
    print("\nHTTP Headers Received:\n")
    
    # Print out specific headers if they exist
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

# Main loop to continuously ask the user for a URL and retrieve the HTTP headers
while 1:
    try:
        # Prompt the user to input a URL
        url = input("B-HTTP-Header-Inspector$ ")
        
        # Exit the program if the user types 'exit'
        if url.lower() == "exit":
            exit(0)  # Exit the program 
        
        else:
            # Get the HTTP headers by calling the get_http_headers function
            headers = get_http_headers(url)
            
            # If headers are returned, print them. Otherwise, inform the user.
            if headers:
                # Convert header keys to lowercase to ensure consistent formatting
                headers = {key.lower(): value for key, value in headers.items()}
                print_info(headers)  # Call function to print headers
            else:
                print("No headers to display.")  # If no headers were found or an error occurred

    except Exception as e:
        # Catch any general exception and print an error message
        print(f"ERROR: {e}")
