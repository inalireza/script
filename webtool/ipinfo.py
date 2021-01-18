import requests

url = "https://api.ip2country.info/ip?"

urlinp = input("Enter Ip : ")

req = requests.get("https://ipinfo.io/" + urlinp + "?token=e21bdf004f5342").text

print (req)
