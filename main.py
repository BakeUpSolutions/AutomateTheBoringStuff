from email.mime.text import MIMEText
from email.mime.image import MIMEImage
from email.mime.application import MIMEApplication
from email.mime.multipart import MIMEMultipart
import smtplib
import keepass_intergration
import os

# Initiate SMTP connection
smtp = smtplib.SMTP('smtp.gmail.com', 587)

# Send an EHLO command
smtp.ehlo()

# Enable transport layer security encryption
smtp.starttls()

# Provide credentials for email
smtp.login(keepass_intergration.entry.username, keepass_intergration.entry.password)

# Create Email Content
msg = MIMEMultipart()
subject = 'Test EMail'
text = """Hi Big Dawg, 
Check out this picture. 

Stay up!

Best,
Benny Baker"""
msg['Subject'] = subject
msg.attach(MIMEText(text))

to = ['Enter recipient']
smtp.sendmail(from_addr=keepass_intergration.entry.username
              , to_addrs=to, msg=msg.as_string())
print("Email Sent")

smtp.quit()
