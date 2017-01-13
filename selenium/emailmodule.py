import smtplib
from email.MIMEMultipart import MIMEMultipart
from email.MIMEText import MIMEText


def sendEmail(username,password):
    server = smtplib.SMTP('smtp.gmail.com',587)
    server.starttls()
    server.login(username,password)


    msg = MIMEMultipart()
    msg['From'] = 'siddimore@gmail.com'
    msg['To'] = 'siddimore@gmail.com'
    msg['Subject'] = 'My First Email With Python'

    body = 'Msg Body'
    msg.attach(MIMEText(body, 'plain'))

#emailmessage = "My First Email With Python"
    text = msg.as_string()
    server.sendmail("siddimore@gmail.com", "siddimore@gmail.com", text)

    server.quit()
