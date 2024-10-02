import subprocess
import optparse
import re 

def get_args():
      parser = optparse.OptionParser()
      parser.add_option("-i","--interface",dest="interface",help="interface to change mac address")
      parser.add_option("-m","--mac",dest="new_mac",help="new mac address")
      (options,arguments)= parser.parse_args()
      if not options:
            print("empty")
      else:
            return options

def change_mac(interface,new_mac):
      subprocess.call(["ipconfig","/all",interface,"down"])
      subprocess.call(["ipconfig","/all",interface,"hw","ethrer",new_mac])
      subprocess.call(["ipconfig","/all",interface,"up"])

def get_cuurent_mac(interface):
      output= subprocess.check_output(["ipconfig","/all",interface])
      current_mac = re.search(r"\w\w:\w\w:\w\w:\w\w:\w\w:\w\w",output)
      if current_mac:
            return current_mac.group(0)
      else:
            print("there is not any mac address")


options = get_args()           
change_mac(options.interface,options.new_mac)
current_mac_addresss = get_cuurent_mac(options.interface)
if options.new_mac == str(current_mac_addresss):
      print("success")
else:
      print("ip address not match")



