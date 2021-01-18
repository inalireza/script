import requests

url = "https://api.ip2country.info/ip?"

urlinp = input("Enter Ip : ")

req = requests.get("https://api.ip2country.info/ip?" + urlinp).text
print (req)
