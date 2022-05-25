


from datetime import datetime
import smtplib
import getpass
import os

path__ = os.path.abspath(os.getcwd())

print(path__)

with open(path__ + "\data.txt", "r") as db:
    data = db.read().split(",")
    emailAdress = data[0]
    emailPassword = data[1]

    recevier = data[2]

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
    
    
    
    
    
    
