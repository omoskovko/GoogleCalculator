from scapy.all import ARP, Ether, srp


def scan_network(network_range):
    arp_request = ARP(pdst=network_range)
    ether_broadcast = Ether(dst="ff:ff:ff:ff:ff:ff")
    packet = ether_broadcast / arp_request

    result, _ = srp(packet, timeout=10, verbose=True, iface_hint=network_range)

    return result


network_range = "192.168.88.1/24"
hosts = scan_network(network_range)
hosts.summary(lambda s, r: r.sprintf("%Ether.src% %ARP.psrc%"))
