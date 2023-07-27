import subprocess
import os
import ipaddress

def ping_ip(ip_address):
    reply = subprocess.run(['ping', '-c', '3', '-n', ip_address],
                           stdout=subprocess.PIPE,
                           stderr=subprocess.PIPE,
                           encoding='utf-8')
    
    if reply.returncode == 0:
        return True, reply.stdout
    else:
        return False, reply.stderr
    
from_ip = ipaddress.ip_address('10.0.0.1')
to_ip = ipaddress.ip_address('10.0.0.6')

for ip in range(int(from_ip),int(to_ip)):
    print(ipaddress.ip_address(ip))