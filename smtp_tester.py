#%% import needed modules
import datetime
import smtplib
from email.mime.text import MIMEText
from dotenv import load_dotenv
import os

#%% SMTP server configuration

# Load environment variables
load_dotenv()

# SMTP server configuration
smtp_server = os.getenv('SMTP_SERVER')
smtp_port = int(os.getenv('SMTP_PORT'))
username = os.getenv('USERNAME')
password = os.getenv('PASSWORD')

#%% Email content
# get current date and time
now = datetime.datetime.now()
sender_email = os.getenv('SENDER_EMAIL')
recipient_email = os.getenv('RECIPIENT_EMAIL')
subject = 'Test Email from Python at :' + now.strftime("%d/%m/%Y %H:%M:%S")
body = 'This is a test email sent from Python script. \n\nSent time is: ' + now.strftime("%d/%m/%Y %H:%M:%S") + '\n\n' + 'Regards,\nPython'

#%% Create a MIMEText object
msg = MIMEText(body)
msg['Subject'] = subject
msg['From'] = sender_email
msg['To'] = recipient_email

#%% Send the email
# Function to send email
def send_email(server, mode='TLS'):
    try:
        server.login(username, password)
        server.sendmail(sender_email, recipient_email, msg.as_string())
        print("Email successfully sent via mode: ", mode)
    except Exception as e:
        print(f"Error sending email: {e}")

# Send the email using TLS or SSL
try:
    if smtp_port == 587:
        with smtplib.SMTP(smtp_server, smtp_port) as server:
            server.starttls()  # Start TLS encryption
            send_email(server, mode='TLS')
    elif smtp_port == 465:
        with smtplib.SMTP_SSL(smtp_server, smtp_port) as server:
            send_email(server, mode='SSL')
    else:
        print("Unsupported port. Use 587 for TLS or 465 for SSL.")
except Exception as e:
    print(f"Error: {e}")
# %%
