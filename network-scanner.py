import scapy.all as scapy

# def scanner(ip):
#       scapy.arping(ip)

def scanner(ip):
      request = scapy.ARP(pdst=ip)
      broadcast = scapy.Ether(dst="ff:ff:ff:ff:ff:ff")
      merge = request/broadcast
      answered_list = scapy.srp(merge,timeout=1,verbose=False)[0]
      unanswered_list = scapy.srp(merge,timeout=1,verbose=False)[1]

      for i in answered_list:
            print(i)
            print("-----------")


scanner("192.168.56.1/24")