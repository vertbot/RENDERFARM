import smtplib
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText

def send_email(subject, body, to_email):
    from_email = "michael.vertefeuille@uconn.edu"
    password = "Donna1234"

    # Create the email
    msg = MIMEMultipart()
    msg['From'] = from_email
    msg['To'] = to_email
    msg['Subject'] = subject
    msg.attach(MIMEText(body, 'plain'))

    # Connect to the server
    server = smtplib.SMTP('smtp.office365.com', 587)
    server.starttls()
    server.login(from_email, password)

    # Send the email
    server.send_message(msg)
    server.quit()

# Example usage
send_email("Test Subject", "This is a test email body.", "vert@uconn.edu")