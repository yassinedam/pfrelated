#!/pyscripts python3
from scapy.all import *
#a=sniff(iface="br-lan",filter="udp && (dst port 65002 or ((ip[6:2]>0)and(not ip [6]=64)))",prn= lambda x:x.show())
a=sniff(iface="br-lan",filter="udp && dst port 65002" ,prn=lambda x:x.show())
a.summary()
#wrpcap("recived.pcap",a)
