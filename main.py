import smtplib
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart
import subprocess
import os
import sys

def email_new(sender, recipient,msg,config):
    message = MIMEMultipart()
    message['Subject'] = 'Server maintainance planned'
    message['From'] = sender
    message['To'] = recipient
    password=os.getenv("PASSWORD")
    body = msg +"\n" + config

    
    message.attach(MIMEText(body, "Plain"))
    with smtplib.SMTP("smtp.office365.com", 587) as server:
        server.starttls()
        server.login(sender,password)
        server.sendmail(sender,recipient, message.as_string())

if __name__ == '__main__':
    sender = sys.argv[1]
    recipient = sys.argv[2] 
    config = sys.argv[3]
    msg = sys.argv[4]
    email_new(sender,recipient,msg,config)

  
    