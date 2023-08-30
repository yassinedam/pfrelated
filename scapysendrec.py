#! /pyscript python
from scapy.all import *
ans,unans=srp(IP(dst="192.168.99.223",ttl=5)/ICMP()/TCP(dport=[21,22,23]))
ans.summary()
unans.summary()
p=srp1(IP(dst="192.168.99.223")/ICMP()/TCP(dport=[21,22,23]))
p.show()
