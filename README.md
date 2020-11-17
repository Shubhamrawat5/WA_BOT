# WHATSAPP-BOT
 to give weather info by "\weather cityname" in the chat like:
<hr>

### \weather delhi
```
Place: delhi
Temperature: 21°C
Condition: Fog
```
<hr>

## Install required libraries
pip install selenium

pip install requests

pip install bs4
<hr>

## Download web driver of your browser
[For chrome browser] https://chromedriver.storage.googleapis.com/86.0.4240.22/chromedriver_win32.zip 

Now set the PATH of this chrome web driver in environment variables (if did then comment line 7 and remove PATH from parameter in line 8

or edit the code, in line 7: PATH="paste here your chrome webdriver location"
<hr>

## READY TO USE!

#### Now run the whatsapp.py script, automatically new chrome will open and whatsapp web will get open, now scan the QR code !
#### chat will be loaded then click on a chat manually (if you want this also to automate then edit and read line 18-20 code
#### now it will start scanning the last message of current chat and if it found a message start with \weather then it will pick the message and search of whatever given after \weather in google and then does web scraping of the weather result of the given place and then automatically write it in the message box and automatically send, if found! otherwise it will send "place is not found!" 
<hr>
