import random 
import time
import subprocess
from colorama import Fore, Back, Style
import os
import sys

#function defined for coloring
def prGreen(skk): print("\033[92m {}\033[00m" .format(skk))
def prYellow(skk): print("\033[93m {}\033[00m" .format(skk))
def prRed(skk): print("\033[91m {}\033[00m" .format(skk))

BOLD = '\033[1m'
def intro1():
    print()
    print(BOLD + f'{Fore.RED}  _     _ ______ _______   _    _  _____  _____ _   __                                            {Style.RESET_ALL}')
    print(BOLD + f'{Fore.RED} | \   | |  ____|__   __| | |  | |/  _  \|  ___| | / /                                            {Style.RESET_ALL}')
    print(BOLD + f'{Fore.RED} | |\  | | |___    | |    | |__| |  / \  | |   | |/ /                                               {Style.RESET_ALL}')
    print(BOLD + f'{Fore.RED} | | \ | |  ___|   | |    |  __  | |___| | |   |   /                                   {Style.RESET_ALL}')
    print(BOLD + f'{Fore.RED} | |  \| | |____   | |    | |  | | |---| | |___|   \    __                                           {Style.RESET_ALL}')
    print(BOLD + f'{Fore.RED} |_|   \_|______|  |_|    |_|  |_|_|   |_|_____|_|\ \  / /                                               {Style.RESET_ALL}')
    print(BOLD + f'{Fore.RED}                                                   \ \/ /                      {Style.RESET_ALL}')
    print(BOLD + f'{Fore.RED}                                                    \__/                            {Style.RESET_ALL}')
    time.sleep(1)
    print(f'{Fore.GREEN}                  PYTHON TOOL KIT ! """ {Style.RESET_ALL}')
    print()
    print()
    time.sleep(0.2)
    print(f'{Fore.CYAN} Repo {Style.RESET_ALL} : https://github.com/nethack ')
    time.sleep(0.2)
    print(f'{Fore.CYAN} Email {Style.RESET_ALL} : greatmates122333@gmail.com')
    time.sleep(0.2)
    print(f'{Fore.CYAN} License {Style.RESET_ALL} : Softwarica')
    print()
    time.sleep(1)
    print(f'{Fore.WHITE} *================================*                              {Style.RESET_ALL}')
    print(f'{Fore.WHITE} |{Fore.YELLOW}       Created By:              {Fore.WHITE}|                                       {Style.RESET_ALL}')
    print(f'{Fore.WHITE} |{Fore.YELLOW}    Great_mates @ Softwarica    {Fore.WHITE}|                                                {Style.RESET_ALL}')
    print(f'{Fore.WHITE} *================================*                                     {Style.RESET_ALL}')

def welcome():
    introList = [intro1]
    subprocess.call(['clear'])
    random.choice(introList)()
    #time.sleep(5)
    #subprocess.call(['clear'])

#main menu function
def __main_menu__():
        prGreen(" --------------------------------------- ")
        prGreen("|   N E T - H A C K    T O O L K I T    |")
        prGreen(" --------------------------------------- ")
        prGreen("| [+] 1 -> ARP Spoofing                 |")
        prGreen("| [+] 2 -> DTP Attack                   |")
        prGreen("| [+] 3 -> BPDU Attack                  |")
        prGreen("| [+] 4 -> MAC Spoofing                 |")
        prGreen("| [+] 5 -> Packet Sniffing              |")
        prGreen("| [+] 6 -> DHCP Starvation              |")
        prGreen("| [!] 0 -> Quit                         |")
        prGreen(" --------------------------------------- ")


#handelling code execution
if __name__ == "__main__":
    if not 'SUDO_UID' in os.environ.keys():
        print(BOLD + f"{Fore.RED} Try running this program with sudo!!!{Style.RESET_ALL}")
        exit()
    #calling welcome function
    welcome()
    time.sleep(2)


while True:

    #calling __main_menu__ function   
    __main_menu__()

    try:
        #taking input from the user
        opt = int(input("[+] Enter Option to Perform: "))

        if opt == 0:
            prRed("[!] Quitting.")
            exit()

        elif opt==2:
            os.system('python3 dtp.py')
            time.sleep(2)
            subprocess.call(['clear'])

        elif opt==3:
            os.system('python3 bpdu.py')
            time.sleep(2)
            subprocess.call(['clear'])

        elif opt == 5:
            interfacee = input("Enter interface to sniff (eth0): ")
            os.system(f'python3 sniffer.py -i {interfacee}')
            time.sleep(2)
            subprocess.call(['clear'])
        
        elif opt == 1:
            os.system('python3 arp_spoofing.py')
            time.sleep(2)
            subprocess.call(['clear'])

        elif opt == 4:
            interface = input("Enter interface name(e.g. eth0): ")
            new_mac = input("Enter new MAC: ")
            os.system(f'python3 mac_spoof.py -i {interface} -m {new_mac}')
            time.sleep(3)
            subprocess.call(['clear'])

        elif opt == 6:
            os.system('python3 dhcp_starve.py')
            time.sleep(2)
            subprocess.call(['clear'])
        
        else:
            prYellow("[!] Invalid Option.")
            time.sleep(2)
            #prRed("[!] Quitting.")
            #subprocess.call(['clear'])
            
            
    except KeyboardInterrupt:
        sys.exit('\n^C\n')



