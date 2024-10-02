import scapy.all as scapy

def scanner(ip):
      scapy.arping(ip)


scanner("192.168.56.1/24")