import requests

# footprinting by checking methods
methodsList = ['POST', 'PUT', 'GET', 'DELETE', 'TRACE', 'TEST']

# looping throught methodsList to find method, status code and reason
for method in methodsList:
	request = requests.request(method, 'Enter target URL: ')
	print(f"Method: {method} \n")
	print(f"Status Code: {request.status_code} \n")
	print(f"Reason: {request.reason} \n")
	
	if method == 'TRACE' and 'TRACE / HTTP/1.1' in request.text:
	print ("Cross Site Tracing(XST) is possible on the target URL") 


# footprinting by checking headers			
headersList = ['Server', 'Date', 'Via', 'X-Powered-By', 'X-Country-Code', 'Connection', 'Content-Length']

# looping through headersList
for header in headersList:
	try:
		# finding header
		result = request.headersList[header]
		print(f"{header} : {result}")
	except Exception as err:
		print(f"{header}: No Details Found")


# finding insecure web server configuration
# if we have a file with target websites
# we can read that file
# please add your target websites URL are in websites.txt file 
targetURLs = open("targetWebsites.txt", "r")

# dictionary that has common web server configurations
webServerConfigurations = {
	"protection_xss": "X-XSS-Protection",
	"options_content_type": "X-Content-Type-Options",
	"transport_security": "Strict-Transport-Security",
	"content_security": "Content-Security-Policy"
}

# looping through the target URL that are read from the text file 'targetWebsites.txt'
for url in targetURLs:
	url = url.strip()
	request = requests.get(url)
	print(f"{url} Report: ")

	# looking for different insecure web server configurations
	# if any insecure config is found it will be printed
	try:
		protection_xss = request.headers[webServerConfigurations.protection_xss]
		if protection_xss != '1; mode = block':
			print(f"{webServerConfigurations.protection_xss} not set properly, it may be possible: {protection_xss}")
	except:
		print(f"{webServerConfigurations.protection_xss} not set, it may be possible")

	try:
		options_content_type = request.headers[webServerConfigurations.options_content_type]
		if protection_xss != 'nosniff':
			print(f"{webServerConfigurations.options_content_type} not set properly, it may be possible: {options_content_type}")
	except:
		print(f"{webServerConfigurations.options_content_type} not set.")

	try:
		transport_security = request.headers[webServerConfigurations.transport_security]
	except:
		print(f"{webServerConfigurations.transport_security} header not set properly, Man-In-The-Middle attack is possible")

	try:
		content_security = request.headers[webServerConfigurations.content_security]
		print(f"{webServerConfigurations.content_security}: ")
	except:
		print(f"{webServerConfigurations.content_security} is missing")