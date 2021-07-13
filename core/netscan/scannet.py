from shutil import *
from subprocess import *
from os import *
import socket
from ipaddress import ip_network, ip_address
from icmplib import *

#NMAP INSTALLATION

#installation guide
def toolInstall():

	install=print(call("sudo apt-get install nmap", shell=True))


def toolScan():
	check1=which("nmap")
	test=print(check1)

	if check1=="/usr/bin/nmap":
		print("[*] NMAP is ready to run")
	
	elif "none":
		print("[*] please install NMAP")
		print()
		toolInstall()

def domain2ip(url):
    host= socket.gethostbyname(url)
    return host

#Scan If The IP is Cloudflare Dist
 
cidrs = ["173.245.48.0/20","103.21.244.0/22","103.22.200.0/22","103.31.4.0/22","141.101.64.0/18","108.162.192.0/18","190.93.240.0/20","188.114.96.0/20","197.234.240.0/22","198.41.128.0/17","162.158.0.0/15","104.16.0.0/12","172.64.0.0/13","131.0.72.0/22"]
 
def is_cloudflare(ip):
    for cidr in cidrs:
        net = ip_network(cidr)
        if (ip_address(ip) in net):
            return True
    return False

#Scan IP Address

def is_server_up(ipinput):
    host=ping((ipinput), count=10, interval=0.2)
    activehost=host.is_alive
    
    return activehost

#portScan
def portScan(url):
    # nmapRun = system("nmap " + url)
    url = domain2ip(url)
    print("")
    print(f"Scanning Server {url}")
    nmapRun = system(f'nmap -T5 -Pn -oG - -p21,22,80,443 {url} --dns-servers 1.1.1.1 | grep -E "(open|filtered|closed)"')
