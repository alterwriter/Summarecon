from core.subdomain import SubdomainScanner
from core.webscan import run_wappalizer
from core.netscan import scannet
from core.util import Misc
from core.log import Log

import sys
import os

class LemonSquash():
    
    def __init__(self, domain):
        self.domain = domain
        self.subdomain_scanner = SubdomainScanner(domain)
        self.network_scanned = []
    
    def do_subdomain_scanning(self):
        Log.info(f"Memulai Subdomain Scanner pada {self.domain}\n")
        self.subdomain_scanner.hackertarget()
        self.subdomain_scanner.subdomains.append(self.domain)

        if self.subdomain_scanner.subdomain_count == 0:
            Log.warning(f"Tidak Ditemukan adanya subdomain pada {self.domain}")
            return None

        for subdomain in self.subdomain_scanner.subdomains:
            Log.info(subdomain.decode())
        
        print("")
        Log.info(f"Total Subdomain Yang ditemukan : {self.subdomain_scanner.subdomain_count}\n")

    def do_web_scanning(self):
        Log.info(f"Memulai Website Scanner pada {self.domain}\n")
        
        for subdomain in self.subdomain_scanner.subdomains:
            if not subdomain.startswith("http://".encode()) or not subdomain.startswith("https://".encode()):
                subdomain = f"http://{subdomain.decode()}"
                run_wappalizer(subdomain)

    def do_net_scanning(self):
        Log.info(f"Memulai Network Scanner pada {self.domain}\n")
        
        for subdomain in self.subdomain_scanner.subdomains:
            ip = scannet.domain2ip(subdomain)
            
            if ip in self.network_scanned:
                continue
            
            if scannet.is_cloudflare(ip):
                continue
            
            # if not scannet.is_server_up(ip):
                # continue
            
            scannet.portScan(ip)
            self.network_scanned.append(ip)

    @staticmethod
    def help():
        Log.info("Jalankan Program dengan perintah : ")
        Log.info(f"python {sys.argv[0]} example.com\n\n")
        # Log.info("Jalankan Program ini sebagai Root User untuk fitur is_server_up")
        exit(0)
    
    @staticmethod
    def dependency_check():
        pass

if __name__ == '__main__':
    
    # if os.getuid != 0:
    #     Log.warning("User bukan root, is_server_up tidak akan dijalankan")

    if len(sys.argv) == 1:
        LemonSquash.help()
    
    lemon = LemonSquash(sys.argv[1])

    lemon.do_subdomain_scanning()
    lemon.do_web_scanning()
    lemon.do_net_scanning()