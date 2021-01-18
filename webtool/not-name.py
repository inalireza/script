import requests
import json
import colorama
from colorama import Fore,init
import random
init(autoreset=True)
response = requests.get("http://168.119.202.31:8000/api/v2/crypto/").text
myjson = json.loads(response)

#print ("Name : ", myjson['data'][0]['name'])

def dash():
    text = "\n==============================================================\n"
    bad_colors = ['BLACK', 'WHITE', 'LIGHTBLACK_EX', 'RESET']
    codes = vars(colorama.Fore)
    colors = [codes[color] for color in codes if color not in bad_colors]
    colored_chars = [random.choice(colors) + char for char in text]
    print(''.join(colored_chars))

for data in myjson['data']:
    print (Fore.YELLOW+"Crypto Name   : ", Fore.LIGHTMAGENTA_EX+data['name'],"\n")
    print (Fore.YELLOW+"Dollar Price  : ", data['dollar_price'],"\n")
    print (Fore.YELLOW+"Toman Price   : ", data['toman_price'],"\n")
    print (Fore.YELLOW+"Daily Change  : ", data['daily_change'],"\n")
    print (Fore.YELLOW+"Weekly Change : ", data['weekly_change'],"\n")
    print (Fore.YELLOW+"Market Cap    : ", data['market_cap'])
    dash()
