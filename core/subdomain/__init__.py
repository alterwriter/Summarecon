from core.util import Requester, HtmlParser, Misc
from core.log import Log

import re
import json
import math
import threading

class SubdomainScanner:

    def __init__(self, domain=None):
        self._domain = domain
        # self.subdomains = set()
        self._subdomains = set()
        self.lock = threading.Lock()
        self.ips = list()
        # self._htmlparser = HtmlParser()
    
    @property
    def subdomains(self):
        return list(set(self._subdomains))
    
    @property
    def domain(self):
        return self._domain
    
    @domain.setter
    def domain(self, domain_):
        self._domain = domain_

    @property
    def subdomain_count(self):
        return len(self.subdomains)
    
    @property
    def ip_list(self):
        if len(self.ips) != 0:
            return list(set(self.ips))
        
        for subdomain in self.subdomains:
            self.ips.append(Misc.domain2ip(subdomain))
        
        return list(set(self.ips))

    @property
    def uniq_ip_count(self):
        return len(self.ip_list)

    def hackertarget(self):
        Log.info("Starting Hackertarget")
        DEBUG = False
        if DEBUG:
            print("Dont forget to start php webserver for debugging process")
            url = "http://127.0.0.1:8083/hackertarget_result.txt"
        else:
            url = "https://api.hackertarget.com/hostsearch/?q={}".format(self._domain)

        r = Requester.get(url)
        raw = r.content.split()
        subdomains = [sub.split(b",")[0].strip() for sub in raw]
        
        self.lock.acquire(timeout=1)
        try:
            self._subdomains.update(set(subdomains))
        finally:
            self.lock.release()
        # return set(subdomains)
        # Log.info("Done Hackertarget")
    
    def entrust(self):
        # FIXME: got 403 response
        Log.info("Starting Entrust")
        url = "https://ctsearch.entrust.com/api/v1/certificates?fields=subjectDN&domain={}&includeExpired=false&exactMatch=false&limit=5000".format(self._domain)
        r = Requester.get(url)
        raw = r.content
        json_data = json.loads(raw)
        subdomains = []
        for i in json_data:
            tmp = re.findall(r"(?:[a-z0-9](?:[a-z0-9-]{0,61}[a-z0-9])?\.)+[a-z0-9][a-z0-9-]{0,61}[a-z0-9]", i.get("subjectDN"))[0]
            subdomains.append(tmp)

        self.lock.acquire(timeout=1)
        try:
            self._subdomains.update(set(subdomains))
        finally:
            self.lock.release()
        Log.info("Done Entrust")

    def threatcrowd(self):
        Log.info("Starting Threadcrowd")
        url = "https://threatcrowd.org/searchApi/v2/domain/report/?domain={}".format(self._domain)
        r = Requester.get(url)
        raw = r.content
        json_data = json.loads(raw)
        subdomains = json_data.get("subdomains")
        
        self.lock.acquire(timeout=1)
        try:
            self._subdomains.update(set(subdomains))
        finally:
            self.lock.release()
        Log.info("Done Threadcrowd")

    def riddler(self):
        Log.info("Starting Riddler")
        url = "https://riddler.io/search/exportcsv?q=pld:{}".format(self._domain)
        r = Requester.get(url)
        raw = r.content
        print(raw.split())

    def certspotter(self):
        Log.info("Starting Certspotter")
        url = "https://api.certspotter.com/v1/issuances?domain={}&include_subdomains=true&expand=dns_names".format(self._domain)
        r = Requester.get(url)
        raw = r.content
        json_data = json.loads(raw)
        subdomains = []
        for i in json_data:
            tmp = i.get("dns_names")[0].strip("*.")
            # if len(tmp) > 1:
            #     [0].strip("*.")
            subdomains.append(tmp)
        
        self.lock.acquire()
        try:
            self._subdomains.update(set(subdomains))
        finally:
            self.lock.release()
        # print(set(subdomains))
        # return set(subdomains)
        Log.info("Done Certspotter")
    
    def threatminer(self):
        Log.info("Starting Threadminer")
        url = "https://api.threatminer.org/v2/domain.php?q={}&rt=5".format(self._domain)
        r = Requester.get(url)
        raw = r.content
        json_data = json.loads(raw)

        if json_data.get("status_code") != "200":
            return None
        
        subdomains = json_data.get("results")
        
        self.lock.acquire()
        try:
            self._subdomains.update(set(subdomains))
        finally:
            self.lock.release()
        # print(set(subdomains))
        # return set(subdomains)
        Log.info("Done Threadminer")

    
    def crtsh(self):
        Log.info("Starting Crtsh")
        url = "https://crt.sh/?q={}".format(self._domain)
        r = Requester.get(url)
        raw = r.content
        html_parser = HtmlParser(raw)
        tag = html_parser.getElementsByTagName(name="td")
        # index = 6
        
        subdomains = list()
        
        for i in range(1, math.floor(len(tag)/6)):
            index = i*6

            if "<br/>" in str(tag[index]):
                tmp = str(tag[index]).split("<br/>")
                tmp[0] = tmp[0].strip("<td>").strip("*.")
                tmp[-1] = tmp[1].strip("</td>").strip("*.")
                subdomains.extend(tmp)
                continue

            subdomains.append(tag[index].getText().strip("*."))
        
        self.lock.acquire()
        try:
            self._subdomains.update(set(subdomains))
        finally:
            self.lock.release()
        # return set(subdomains)
        Log.info("Done Crtsh")


    def dnsdumpster(self):
        """ Not implemented yet """
        subdomains = list()
        self.lock.acquire()
        try:
            self._subdomains.update(set(subdomains))
        finally:
            self.lock.release()
        pass

if __name__ == '__main__':
    sub = SubdomainScanner("tokopedia.com")
    sub.hackertarget()
    print("Subdomain : ", sub.subdomains)
