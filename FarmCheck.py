import smtplib
import requests
from email.mime.text import MIMEText
import ssl
import time

# Configuration
website_url = 'http://137.99.93.113:8080/#/monitor'
email_sender = 'Vert@uconn.edu'
email_receiver = 'Vert@uconn.edu'
email_subject = 'Render Farm Down'
email_body = f'The website {website_url} is down.'
smtp_server = 'mail.smtp2go.com'
smtp_port = 2525
smtp_username = 'vert'
smtp_password = '8ceZFAwK7Qj5xkdf'

def send_email():
    msg = MIMEText(email_body)
    msg['Subject'] = email_subject
    msg['From'] = email_sender
    msg['To'] = email_receiver
    context = ssl.create_default_context()

    with smtplib.SMTP(smtp_server, smtp_port) as server:
        server.starttls(context=context)
        server.login(smtp_username, smtp_password)
        server.sendmail(email_sender, email_receiver, msg.as_string())
    time.sleep(300)

def check_website():
    try:
        response = requests.get(website_url)
        if response.status_code != 200:
            send_email()
            print ('Website is down')
        else:
            print ('Website is up')
    except requests.RequestException:
        send_email()
        print ('Website is down')
    time.sleep(60)

if __name__ == '__main__':
    while True:
        check_website()


