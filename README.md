# Login-Info

Used Modules in Project:

-datetime
-smtplib
-getpass

No need to install any packages.

How to use it;

First Create a Gmail account 

----- THIS ACCOUNT IS JUST GONNA SEND YOU EMAILS SO YOU DONT NEED TO ADD ANY PERSONAL INFO ----- 

----- JUST KNOW THE ADDRESS AND PASSWORD -----


In your knew created account go to "Manage your Google Account => Security" and close the of the bottom of the page set "Insecure application access" ON.
With this you will give permission to smtplib module to get access to your Gmail account.

When you run the code it will want 3 inputs;

First input is goind to be your new created account's email address. For example:
    example@gmail.com

Second input is going to be your new created account's password. For example:
    123456789Example
    
And last input is going to be your Main Email account. The Login infos are going to send to this email address by your new created account.

And also we must make a trigger on our computer for our script.

When you login to your computer the code will be triggered.

Check this link to see how to do it;

https://superuser.com/questions/15596/automatically-run-a-script-when-i-log-on-to-windows/797635#797635


After you set everything it will work smoothly.

Here is some photos of Task Scheduler if you dont understand;

![1](https://user-images.githubusercontent.com/92454444/169260327-f201406b-9840-4e5d-b856-3b4e37d78410.PNG)

Create Task

![2](https://user-images.githubusercontent.com/92454444/169260497-4a920f7c-342c-4f3e-a775-ebb205803cab.png)

Name the trigger as you like and go to "Triggers" tab.

![3](https://user-images.githubusercontent.com/92454444/169260639-e2d74778-b19c-485f-9730-bab85e8c8da3.png)

After that hit new.

![Inked4_LI](https://user-images.githubusercontent.com/92454444/169260747-b0579314-2bc3-4546-a43c-b91e77f39f3c.jpg)

Then set the "Start Task" to "When Signed In".

![5](https://user-images.githubusercontent.com/92454444/169260989-83688cde-9447-4220-bf7f-77c0db86534c.png)

Then go to "Actions" tab and create new action.

![6](https://user-images.githubusercontent.com/92454444/169261184-9a556d37-b724-483f-a61b-e22660388858.png)

And Write the path of Alert.py that you installed.

![7](https://user-images.githubusercontent.com/92454444/169261336-e3ac181a-b83a-44ee-8f8a-652b1019394e.png)

Your Trigger must be looks like this.





