#! /pyscripts python
from scapy.all import *
#pkt=rdpcap("/pyscript/toBeSent.pcap")
pkt=rdpcap("/pyscript/Hello.pcap")
#s=send(IP(dst="192.168.99.255")/UDP(sport=65002,dport=65002)/Raw("Hello device!!"),iface="br-lan",count=3)
#s=send(pkt,iface="br-lan",count=3)
#wrpcap("Hello.pcap",IP(dst="192.168.99.255")/UDP(sport=65002,dport=65002)/Raw("Hello device this is supposed tobr frargmented so hopefully it reaches!!"))
for i in range(len(pkt)):
	if len(pkt[i])>45:
		frgs=fragment(pkt[i],fragsize=45)
		s=send(frgs,iface="br-lan")
