from email.message import EmailMessage
from email_password import password
import ssl
import smtplib
import time

email_sender = ' sender@email.com'
email_password = password
email_receiver = ' receiver@email.com'

subject = "Python Email Sender Test"
body = """
Hey, I'm testing python email sender. Wish me luck.
"""


def send_email():
    em = EmailMessage()
    em['From'] = email_sender
    em['To'] = email_receiver
    em['Subject'] = subject
    em.set_content(body)

    context = ssl.create_default_context()

    with smtplib.SMTP_SSL('smtp.gmail.com', 465, context=context) as smtp:
        smtp.login(email_sender, email_password)
        smtp.sendmail(email_sender, email_receiver, em.as_string())


if __name__ == '__main__':
    time.sleep(0.5)
    print("Initiating_Email_Sender")

    count = 3
    for c in range(count):
        time.sleep(1)
        print(c+1)

    time.sleep(0.5)
    send_email()
    print("Email Successfully Sent!")




