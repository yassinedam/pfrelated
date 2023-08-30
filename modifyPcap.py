#! /pyscript puthon3
from scapy.all import *
from scapy.utils import PcapWriter
packets=rdpcap("/pyscript/reassmbledpackets/reassembled-1-bsd.pcap")
new_packets=PcapWriter("/pyscript/toBeSent.pcap",append=True,sync=True)
for p in packets:
#	p[Ether].dst="08:00:27:da:1d:79"
#	p[Ether].src="60:a4:b7:c2:ce:50"
	p[IP].dst="192.168.99.255"
	p[IP].src="192.168.99.1"
#	p[IP].len=3990
	new_packets.write(p)
