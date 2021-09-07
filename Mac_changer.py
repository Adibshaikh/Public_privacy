# It changes MAC address in Linux (Kali Linux)
#!/usr/bin/env pyhon
import optparse
import subprocess
import re

def getargs():
    parser = optparse.OptionParser()
    parser.add_option("-i", "--interface", dest="interface", help="The interface you want to change")
    parser.add_option("-m", "--newmac", dest="newmac", help="Enter the new mac address")
    (options, arguments) = parser.parse_args()
    if not options.interface:
        #code to handle error related to interface
        parser.error("[-] Please specify an interface, use --help for more info.")
    elif not options.newmac:
        #code to handle error related to MAC
        parser.error("[-] Please specify a MAC address, use --help for more info.")
    return options

def changemac(interface, newmac):
    print("[+] Changing MAC address for " + interface)
    print("[+] Your new MAC address will be " + newmac)
    subprocess.call(["ifconfig", interface, "down"])
    subprocess.call(["ifconfig", interface, "hw", "ether", newmac])
    subprocess.call(["ifconfig", interface, "up"])


def get_cur_mac(interface):
    ifconfig_result = subprocess.check_output(["ifconfig", interface])
    mac_address_search = re.search(r"\w\w:\w\w:\w\w:\w\w:\w\w:\w\w", str(ifconfig_result))
    if mac_address_search:
        return mac_address_search.group(0)
    else:
        print("[-] Sorry ,could not read the Mac Address")

options = getargs()

cur_mac = get_cur_mac(options.interface)
print("[+] Your current Mac is = " + str(cur_mac))

changemac(options.interface, options.newmac)

cur_mac = get_cur_mac(options.interface)

# if options.newmac == cur_mac:
#     print("[-] Your Mac address hasn't been changed, you have entered your old Mac Address.")
if cur_mac == options.newmac:
    print("[+] MAC address has been changed to = " + cur_mac)
else:
    print("[-] Mac address did not get changed")
