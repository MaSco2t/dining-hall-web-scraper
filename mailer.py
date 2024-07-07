from dotenv import load_dotenv

import os
import smtplib
from email.message import EmailMessage

def send_email(email_subject,email_content):  
    
    load_dotenv()
    email_sender = os.getenv("SENDER")
    email_receiver = os.getenv("RECEIVER")
    gmail_address = os.getenv('ACCOUNT_ADDRESS')
    gmail_password = os.getenv("ACCOUNT_PASSWORD")

    msg = EmailMessage()
    msg['Subject'] = email_subject
    msg['From'] = email_sender
    msg['To'] = email_receiver
    msg.set_content(email_content)

    smtp_obj = smtplib.SMTP("smtp.gmail.com",587)
    smtp_obj.starttls()
    smtp_obj.login(gmail_address,gmail_password)
    smtp_obj.send_message(msg)