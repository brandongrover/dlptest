import sys, os
sys.path.append(f'{os.getcwd()}\data_generator')
import smtplib
from email.mime.text import MIMEText
from generate_canadian_pii import generate_fake_sin, generate_fake_name

smtp_ssl_host = 'localhost'
smtp_ssl_port = 25
sender = 'test@dlptest-fake.com'
targets = ['test@dlptest-fake.com']

msg = MIMEText(f'{generate_fake_sin()} {generate_fake_name()}')
msg['Subject'] = f'{generate_fake_sin()} {generate_fake_name()}'
msg['From'] = sender
msg['To'] = ', '.join(targets)

server = smtplib.SMTP(smtp_ssl_host, smtp_ssl_port)
server.sendmail(sender, targets, msg.as_string())
server.quit()