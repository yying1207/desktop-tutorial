import requests
import bs4
import smtplib
import os


email_add = os.environ.get("EMAIL_ADD") # get the email address from an environment variable named "EMAIL_ADD". This allows you to keep your email address secure and not hard-code it in the script. You can set this environment variable in your operating system or in your development environment before running the script.
email_pass = os.environ.get("EMAIL_PASS") # get the email password from an environment variable named "EMAIL_PASS". This is a secure way to handle sensitive information like passwords, as it prevents them from being exposed in the code. You can set this environment variable in your operating system or in your development environment before running the script.
def send_email():
    s = smtplib.SMTP('smtp.gmail.com', 587) # create an SMTP object to connect to the Gmail SMTP server on port 587
    s.starttls() # start TLS encryption for secure communication
    s.login(email_add, email_pass) # log in to the email account using the provided email address and password
    subject = "Price fell down!"
    body = "Check the amazon link: https://www.amazon.in/dp/B0CGLZ5Z8P?th=1"
    msg = f"Subject: {subject}\n\n{body}" # create the email message with the subject and body
    s.sendmail(email_add, email_add, msg) # send the email from the email address to itself with the constructed message
    print("Email has been sent!") # print a confirmation message after sending the email
    s.quit() # close the connection to the SMTP server

producturl = "https://www.amazon.in/dp/B0CGLZ5Z8P?th=1"

resp = requests.get(producturl, timeout=5)
print (resp.status_code) # 200 means the website is accessible and working fine, while 404 means the website is not found or inaccessible. You can also check for other status codes to get more information about the website's response.
print(resp.text) # content of the website page



# bs module is used to Find a html/css object
soup = bs4.BeautifulSoup(resp.text)

elems = soup.select("#priceblock_ourprice") 
"""
1. Using F12 to find out the text, right click on the text and select "Inspect" to find the HTML element that contains the price. 
2. Then, right click on the element in the HTML code and select "Copy" -> "Copy selector" to get the CSS selector for that element. 
3. In this case, the CSS selector for the price is "#priceblock_ourprice". You can use this selector in the soup.select() method to extract the price from the HTML content.
"""

try:
    if elems[0].text < "₹ 1,999.00":
        send_email() # if the price of the product is less than ₹ 1,999.00, the send_email() function will be called to send an email notification about the price drop.
except Exception as e:
    send_email()