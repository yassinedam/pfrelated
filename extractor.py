from scapy.all import *
pkts = rdpcap("/pyscript/toBeSent.pcap")
stripped_pkt = [pkt[Raw].load for pkt in pkts]
wrpcap("/pyscript/stripped_toBeSent.pcap",stripped_pkt)

