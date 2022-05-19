
from datetime import datetime
import smtplib
import getpass


emailAdress = input("Sender email address:\n")
emailPassword = input("Sender email password:\n")

recevier = input("recevier email address:\n")

user = getpass.getuser()
now = datetime.now()

currentTime = now.strftime("%H:%M:%S")


with smtplib.SMTP('smtp.gmail.com', 587) as smtp:
    smtp.ehlo()
    smtp.starttls()
    smtp.ehlo()
    
    smtp.login(emailAdress, emailPassword)
    
    subj= 'Logged In!'
    body = f'You logged in as {user}, at {currentTime}'
    
    msg = f'Subject: {subj}\n\n{body}'
    smtp.sendmail(emailAdress, recevier, msg)
    
    
    