import requests
import colorama
dat = input("Enter Url Or For Qr Code : ")
response = requests.get("https://api.qrserver.com/v1/create-qr-code/?size=150x150&data=" + dat).text
print (response)