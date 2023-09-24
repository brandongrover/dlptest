import sys, os
sys.path.append(f'{os.getcwd()}\data_generator')
import smtplib
from email.mime.text import MIMEText
import ssl
from generate_canadian_pii import generate_fake_sin, generate_fake_name

# Configs
sender = 't6784702@gmail.com'
server = 'localhost'
port = 2526
targets = ['fake_target@dlptest.com']
msg = MIMEText(f'{generate_fake_sin()} {generate_fake_name()}')
subject = f'{generate_fake_sin()} {generate_fake_name()}'

def send_email(user, server, port, recipient, subject, body):
    FROM = user
    TO = recipient if isinstance(recipient, list) else [recipient]
    SUBJECT = subject
    TEXT = body
    message = """From: %s\nTo: %s\nSubject: %s\n\n%s
    """ % (FROM, ", ".join(TO), SUBJECT, TEXT)
    try:
        server = smtplib.SMTP(server, port)
        server.sendmail(FROM, TO, message)
        server.close()
        print('successfully sent the mail')
        print(msg)
    except:
        print("failed to send mail")

send_email(sender, server, port, targets, subject, msg)