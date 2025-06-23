import shodan  # Import the Shodan library

API_KEY = "fVTkGNfKFrX74ryL0Ge8IP0x7uz3qn03"  # Replace with your real Shodan API Key

# Initialize Shodan API
api = shodan.Shodan(API_KEY)

try:
    # Search for open webcams (common webcam banners)
    query = 'webcamXP'
    results = api.search(query)

    print(f"Total webcams found: {results['total']}")  # Total devices found

    # Loop through each webcam device
    for result in results['matches']:
        print("="*40)
        print(f"IP: {result['ip_str']}")  # Device IP address
        print(f"Port: {result['port']}")  # Port number, often 8080 or 81
        print(f"Country: {result.get('location', {}).get('country_name', 'n/a')}")  # Country location
        print(f"City: {result.get('location', {}).get('city', 'n/a')}")  # City (if available)
        print(f"ISP: {result.get('isp', 'n/a')}")  # Internet Service Provider
        print("----- Banner -----")
        print(result['data'])  # Banner includes info like software type, login prompt, etc.

except shodan.APIError as e:
    print(f"Shodan error: {e}")  # Handles wrong API key or rate limits

