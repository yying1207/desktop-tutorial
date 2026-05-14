import smtplib
from email.mime.text import MIMEText

smtp_server = "smtp.gmail.com"
port = 587 # For TLS
sender_email = "thenoobgunmaster@gmail.com"
receiver_email = "the noobgunmaster#gmail.com"
message = "Hello, this is an automated message."

# Create a MIMEText object for the email content
msg = MIMEText(message)
msg['Subject'] = 'Automated Email'
msg['From'] = sender_email
msg['To'] = receiver_email

# Set up the connection to the SMTP server
with smtplib.SMTP(smtp_server, port) as server:
    # Start TLS encryption
    server.starttls()

    # Login to your Gmail account
    password = input("Enter your Gmail password and press Enter: ")
    server.login(sender_email, password)

    # Send the email
    server.sendmail(sender_email, [receiver_email], msg.as_string())