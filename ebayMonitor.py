import requests
import time
from bs4 import BeautifulSoup
import json
import ssl
import smtplib
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart

with open('config.json') as f:
    data = json.load(f)

ebayURL = data["ebayURL"]
timewait = data["timewaitSeconds"] # Make sure to set timeout to around 10 minutes+ to avoid getting captcha. Timewait is in seconds.
gmailEmail = data["gmailEmail"]
gmailPassword = data['gmailPassword']
recipientEmail = data ["recipientEmail"]

headers = {'accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9',
    'accept-encoding': 'gzip, deflate, br',
    'accept-language': 'en-US,en;q=0.9',
    'sec-fetch-dest': 'document',
    'sec-fetch-mode': 'navigate',
    'sec-fetch-site': 'none',
    'upgrade-insecure-requests': '1',
    'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/87.0.4280.88 Safari/537.36'}

def monitor(url, timeout):
    global priceSecondary
    while True:
        pagePrimary = requests.get(url, headers = headers).text
        soup = BeautifulSoup(pagePrimary, 'lxml')
        pricePrimary = soup.find('div', class_="notranslate").get_text()
        
        time.sleep(int(timeout))
        
        pageSecondary = requests.get(url, headers = headers).text
        soupSecondary = BeautifulSoup(pageSecondary, 'lxml')
        priceSecondary = soupSecondary.find('div', class_="notranslate").get_text()        
        
        if str(pricePrimary) != str(priceSecondary):
            
            print("Price Change !")
            alert()
       
       
       
       
def alert():  
    context = ssl.create_default_context()
    msgRoot = MIMEMultipart('related')
    msgRoot['Subject'] = 'Ebay Price Updated'
    msgRoot.preamble = 'Multi-part message in MIME format.'
    msgAlternative = MIMEMultipart('alternative')
    msgRoot.attach(msgAlternative)
    msgText = MIMEText('Alternative plain text message.')
    msgAlternative.attach(msgText)
    msgText = MIMEText(f"""Hello,
<br>
This email is notify you that {ebayURL} price just changed. It is now {priceSecondary}                       
<br>
<br>
Regards
<br>
The Wali Ul Asr Coding Club
""", 'html')
    msgAlternative.attach(msgText)
    context = ssl.create_default_context()
    with smtplib.SMTP_SSL("smtp.gmail.com", 465, context=context) as server:
        server.login(gmailEmail, gmailPassword)
        server.sendmail(gmailEmail, recipientEmail, msgRoot.as_string())
        server.quit()
    print("Email Has Been Sent To The Recipient") 

        
monitor(ebayURL, timewait)