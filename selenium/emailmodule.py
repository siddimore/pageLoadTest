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

    html = "<html><body><table><tr><td>name</td><td>age</td><td>dob</td<tr></table></body></html>"
    msg1 = MIMEText(html, 'html')
    msg = MIMEMultipart("test")
    msg.attach(msg1)
#emailmessage = "My First Email With Python To Booboo I love You!!"
    text = msg.as_string()

    # text = "Hi!\nHow are you?\nHere is the link you wanted:\nhttp://www.python.org"
    # html = """\
    # <html>
    #   <head></head>
    #   <body>
    #     <p>Hi!<br>
    #        How are you?<br>
    #        Here is the <a href="http://www.python.org">link</a> you wanted.
    #     </p>
    #   </body>
    # </html>
    # """
    #
    # # Record the MIME types of both parts - text/plain and text/html.
    # part1 = MIMEText(text, 'plain')
    # part2 = MIMEText(html, 'html')
    #
    # # Attach parts into message container.
    # # According to RFC 2046, the last part of a multipart message, in this case
    # # the HTML message, is best and preferred.
    # msg.attach(part1)
    # msg.attach(part2)
    server.sendmail("siddimore@gmail.com", "siddimore@gmail.com", msg.as_string())
    # server.sendmail("siddimore@gmail.com", "luxiaoxue@gmail.com", text)

    server.quit()
