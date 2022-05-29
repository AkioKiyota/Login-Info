
from datetime import datetime
import smtplib
import getpass

#  --FIRST VARIABLE--
emailAdress = 'example@gmail.com'

#  --SECOND VARIABLE--
emailPassword = '123456789Example'

#  --THIRD VARIABLE--
recevier = 'example1@gmail.com'

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
    
    
    
