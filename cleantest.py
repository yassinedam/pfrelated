# !/pyscript python
from scapy.all import *
pkt =  rdpcap("/pyscript/toBeSent.pcap")
for p in pkt:
	q = p.copy()
	del(q[IP].len)
	del(q[IP].chksum)
#	del(q[IP].dst)
wrpcap("/pyscript/proto.pcap",q)
