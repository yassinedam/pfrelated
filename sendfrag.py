#! /pyscrpit python3
from scapy.all import *
#packets = rdpcap("/pyscript/toSend.pcap")
text_pkt = open("/pyscript/data/newfragmenteddata.txt")
data = text_pkt.read()
packets = IP(dst="192.168.99.255")/UDP(sport=65002,dport=65002)/Raw(data)
wrpcap("/pyscript/data/toSendFinale.pcap",packets)
pkts = rdpcap("/pyscript/data/toSendFinale.pcap")
for i in range(len(pkts)):
	if len(pkts[i])>1200:
		frags=fragment(packets[i],fragsize=1200)
		send(frags,iface="br-lan")
	else:
		send(pkts[i],iface="br-lan")
