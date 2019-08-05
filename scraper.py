import requests
from bs4 import BeautifulSoup
import re
import smtplib

URL = 'https://www.amazon.in/Razer-Blade-15-Smallest-i7-8750H/dp/B07HPQPNV1/ref=sr_1_1?keywords=razer+blade&qid=1565002292&s=electronics&sr=1-1'
headers = {"User-Agent": 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/75.0.3770.142 Safari/537.36'}

req = requests.Session()
res = req.get(URL, headers=headers)

def get_price():
    #page = requests.get(URL, headers=headers)
    soup = BeautifulSoup(res.text, features='html.parser')

    title = soup.find(id="productTitle").get_text()
    price = soup.find(id="priceblock_ourprice").get_text()
    price = float(re.sub('\,', '',price[2:]))
    
    if(price < 150000):
        send_mail(price,title)
   
    print(price)
    print(title.strip())

def send_mail():
    server = smtplib.SMTPL('smtp.gmail.com', 587)

   # server.connect('smtp.gmail.com')
    server.ehlo()
    server.startls()
    server.ehlo()

    try:
        server.login('email', 'password')
        subject = 'Price fell down!'
        body = 

    msg = f"Subject: {subject}\n\n{body}"

    server.sendmail(
        'sender email',
        'reciever email',
        msg
    )
    print('Hey email has been sent!')

    server.quit()

check_price()

while(True):
    check_price()
    time.sleep(60*60*60)
