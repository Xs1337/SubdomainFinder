import requests, sys, os, colorama
from colorama import Fore, Back, Style

os.system("clear")

print(f"""{Style.BRIGHT + Fore.RED}
 ██████╗ ██████╗  █████╗  ██████╗  ██████╗ ███╗   ██╗███████╗ ██████╗ ██████╗  ██████╗███████╗   ██╗ ██████╗ 
  ██╔══██╗██╔══██╗██╔══██╗██╔════╝ ██╔═══██╗████╗  ██║██╔════╝██╔═══██╗██╔══██╗██╔════╝██╔════╝   ██║██╔═══██╗
  ██║  ██║██████╔╝███████║██║  ███╗██║   ██║██╔██╗ ██║█████╗  ██║   ██║██████╔╝██║     █████╗     ██║██║   ██║
  ██║  ██║██╔══██╗██╔══██║██║   ██║██║   ██║██║╚██╗██║██╔══╝  ██║   ██║██╔══██╗██║     ██╔══╝     ██║██║   ██║
  ██████╔╝██║  ██║██║  ██║╚██████╔╝╚██████╔╝██║ ╚████║██║     ╚██████╔╝██║  ██║╚██████╗███████╗██╗██║╚██████╔╝
  ╚═════╝ ╚═╝  ╚═╝╚═╝  ╚═╝ ╚═════╝  ╚═════╝ ╚═╝  ╚═══╝╚═╝      ╚═════╝ ╚═╝  ╚═╝ ╚═════╝╚══════╝╚═╝╚═╝ ╚═════╝ 

{Fore.YELLOW}\tSubdomain Finder | Author: Xs7
""")

target = input(Fore.WHITE+"Enter domain : ")

api = "https://api.hackertarget.com/hostsearch/?q="+target
req = requests.get(api)
err_msg = "error invalid host"

if req.status_code==200 and req.text != err_msg:
    subdo_res = req.text.strip().split("\n")
    subdo_count = 0
    subdo = open("subdo_"+target+".txt", "w")
    
    for res in subdo_res:
        subdo_count += 1
        res_domain, res_ip = res.split(",")
        subdo.write(res_domain + "\n")
    subdo.close()
    
    print(Fore.GREEN+f"Total subdomain found: {subdo_count}")
else:
    sys.exit(0)
    os._exit(0)