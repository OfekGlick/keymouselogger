# SpyWare - First attempt
This summer (Summer of 2021) I attempted to write a simple key and mouse logger which works the following way.<br>
`keylogger.py` is the module responsible for logging pressed keys on the keyboard, it contains a class called `KeyLogger` which receives an email address to send the logs and the password of the email, alongside the interval in which to recored the keys pressed.<br>
`mouselogger.py` is the module responsible for recording screen activity according to mouse clicks. Same as `KeyLogger`, `MouseLogger` receives an email address to send the logs and the password of the email.<br>
`master.py` is the main script, instantaining both objects and orchastrating the activity between them along side receiving initial data and in the future also disabing security settings of the "victim".


This script was written for educational and entertainment purposes only.
This script was never used to actually spy on anyone and please do not use it for those purposes.
This script is elementry and makes no attempt to hide itself.
