import smtplib
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart
import subprocess
import os

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
    sender = 'vaibhavk0011@outlook.com'
    recipient = 'khandekarv0@gmail.com'
    config = subprocess.getoutput(['lscpu'])
    msg = "Service XYZ has planned maintenance on Saturday from 14:00 till 17:00 CET"
    email_new(sender,recipient,msg,config)