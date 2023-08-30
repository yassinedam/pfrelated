#! /pyscript pyton3
from scapy.all import *
from scapy.all import PcapReader
#def func(value):
#	return ''.join(value.split('\n')) 
#pkt = rdpcap("/pyscript/reassmbledpackets/reassembled-1-bsd.pcap")
pkt = PcapReader("/pyscript/reassmbledpackets/reassembled-1-bsd.pcap")
pdata=str(pkt.recv(3990)[Raw].load)
data = open("data.txt","w+")
#p=pkt[0]
tdata=""
#for i in range(len(pkt)):
#	if TCP in pkt[i]:
#		pdata=str(pkt[i][TCP].payload)
#	elif Raw in pkt[i]:
#		pdata=str(pkt[i][Raw].load)
#	elif TLS in pkt[i]:
#		pdata= str(pkt[i][TLS].msg)
#	else:
#		pdata="keep trying"
#	tdata=tdata+pdata
data.write(pdata)
#wrpcap("toSend.pcap",IP(dst="192.168.99.255")/UDP(sport=65002,dport=65002)/Raw(pdata))
