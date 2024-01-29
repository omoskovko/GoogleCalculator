import nmap3, sys

target = sys.argv[1]
nm = nmap3.NmapHostDiscovery()
print("Scanning.....")
results = nm.nmap_portscan_only(target)
print(results)
