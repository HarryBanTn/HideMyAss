from pystyle import Colors , Colorate
from time import sleep
import pyshorteners
print(Colorate.Horizontal(Colors.red_to_green,"""
  _   _ _     _          __  __              _
| | | (_) __| | ___    |  \/  |_   _       / \   ___ ___
| |_| | |/ _` |/ _ \   | |\/| | | | |     / _ \ / __/ __|
|  _  | | (_| |  __/   | |  | | |_| |    / ___ \ \__ \__ \\
|_| |_|_|\__,_|\___|___|_|  |_|\__, |___/_/   \_\___/___/
                  |_____|      |___/_____| 
                  
                  \t\t\t*** Coded_By_Nidhal ***               
"""))
def url_check(link):
    if link[0:7]=="http://" or link[0:8]=="https://" :
        pass
    else:
        print(Colors.red+"Invalid URL Please use http or https Links And Try Agin :( ")
        exit()
url=str(input(Colors.gray+"Paste Your Phishing URL here (with http or https) > "))
url_check(url)
sleep(1)
print(Colors.green+"Processing and Modifing Phishing URL ... ")
shrt=pyshorteners.Shortener()
short=shrt.isgd.short(url)
shorter=short[8:len(short)]
print(Colors.cyan+"Mask_Domain :\nType Any Domain to mask the Phishing URL (with http or https), ex: https://facebook.com, http://anything.org :  ")
FakeDomain=str(input("=> "))
url_check(FakeDomain)
print(Colors.yellow+"\nType social engineering words like (free-fire-diamond, pubg-unlimited-uc ...)")
print(Colors.red+"Don't use space just use '-' or '+' between social engineering words only , ok!")
PhisherWords=input("=> ")
print(Colors.purple+"\nMasking Your Link...")
LastThing=FakeDomain+"-"+PhisherWords+"@"+shorter
print(Colors.green+"Here is the Your Fucking Hiden URL : ",LastThing)