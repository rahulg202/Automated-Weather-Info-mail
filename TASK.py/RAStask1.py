import requests
from bs4 import BeautifulSoup
import smtplib,ssl,getpass

from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
import datetime
now=datetime.datetime.now()

city = input("ENTER the city name \n")
info=''
 
url = "https://www.google.com/search?q="+"weather"+city
raw_data = requests.get(url).content
 
soup = BeautifulSoup(raw_data, 'html.parser')
temp = soup.find('div', attrs={'class': 'BNeawe iBp4i AP7Wnd'}).text
time_sky = soup.find('div', attrs={'class': 'BNeawe tAd8D AP7Wnd'}).text
 
data = time_sky.split('\n')
time = data[0]
sky = data[1]
 
listdiv = soup.findAll('div', attrs={'class': 'BNeawe s3v9rd AP7Wnd'})
strd = listdiv[5].text
 
pos = strd.find('Wind')
other_data = strd[pos:]

info+=("Temperature is:"+ temp +"\n"+'<br>'+ "Time: "+time+"\n"+"<br>"+"Sky is "+sky+"\n"+'<br>'+other_data+"\n")


info+=('<br>-----<br>')
info+=('End of Message')      

smtp_server="smtp.gmail.com"
port=587

sender_email="rahulguptabruzo@gmail.com"
receiver_email="gpoonam342@gmail.com"
message=MIMEMultipart()
message["Subject"]="Weather Report of"+city+"Dated: "+str(now.day)
message["From"]=sender_email
message["To"]=receiver_email

message.attach(MIMEText(info,'html'))
password=getpass.getpass(prompt="Enter your password: ")

context=ssl.create_default_context()

server=smtplib.SMTP(smtp_server,port)
server.starttls(context=context) 
server.login(sender_email,password)
print("Successful\n")

server.sendmail(sender_email,receiver_email,message.as_string())