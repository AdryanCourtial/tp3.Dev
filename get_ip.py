import psutil

def ip():
    interfaces = psutil.net_if_addrs()
    for interface, addrs in interfaces.items():
        for addr in addrs:
            if addr.family == 2 and 'Wi-Fi' in interface:
                print(addr.address)