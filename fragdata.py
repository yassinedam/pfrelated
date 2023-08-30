# ! /pyscript python3
from scapy.all import *
pkt = rdpcap("/pyscript/toBeSent.pcap")
#frags = [] 
for i in range(len(pkt)) :
	if len(pkt)>1500 :
		frags=fragment(pkt[i],fragsize=1500)
		send(frags,iface="br-lan")
#		print(type(frags))
		wrpcap("/pyscript/data/fragmenteddata.pcap",frags)
#		print(frags)
#		fraglst.append(frags)
	else :
		wrpcap("/pyscript/data/fragmenteddata.pcap",pkt[i])
#print(frags)
#for i in range(len(frags)):
#	print(frags[i])

