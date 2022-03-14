## SQLi scanner **
##Author: Nancy 

#Creating a python script to help sumbit forms and analyse the response using mechanise

#getting mechanise module
import mechanize

#providing URL from where we will obtain the response after submitting form
url = input("Enter URL")
	attack_no =1 

#read the attack vecotrs from the file 
with open ('attack_vectors.txt')	as v:

#sending request with each attack vector
For line in v:
   browser.open(url)
   browser.select_form(nr = 0)
   browser[“id”] = line
   res = browser.submit()
content = res.read()

#The following line of code will write the response to the output file.
output = open(‘response/’ + str(attack_no) + ’.txt’, ’w’)
output.write(content)
output.close()
print attack_no
attack_no += 1


'''
Reference
https://www.tutorialspoint.com/python_penetration_testing/python_penetration_testing_sqli_web_attack.htm#:~:text=The%20SQL%20injection%20is%20a,connected%20with%20the%20web%20applications.
