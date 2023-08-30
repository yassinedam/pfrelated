#! /pyscript python
from scapy.all import *
p=AsyncSniffer()
p.start()
time.sleep(5)
result = p.stop()
wrpcap("try3.pcap",result)
