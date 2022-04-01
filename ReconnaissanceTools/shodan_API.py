import os
import shodan
import sys

# API Key needs to be added to the Environment Variable prior to use.
api_key = os.environ['SHODAN_API_KEY']
api = shodan.Shodan(api_key)

# Takes the first argument (IP Address)provided when calling the script.
ip_address = sys.argv[1]

# Implement a TRY/CATCH to catch any errors that may occur.
try:
    host = api.host(ip_address)

    print("-------------------------------------------------------------------------")
    print("Organisation:", host['org'])
    print("IP Address:", host['ip_str'])
    print("Country Name:", host['country_name'])
    print("Domains:", host['domains'])
    print("Host Name:", host['hostnames'])
    print("Operating System:", host.get('os','n/a'))
    print("-------------------------------------------------------------------------")
    for item in host ['data']:
        print("""
        * Product: {}
        * Port: {}
        * Transport: {}""".format(item.get('product'),item['port'],item['transport']))

    print("\nLast Shodan Scan:", host['last_update'])

except Exception as e:
    print('Error: {}'.format(e))