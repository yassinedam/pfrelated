#! /pyscript python3
from scapy.all import *
sniff(count=2,filter="udp")
