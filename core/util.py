#!/usr/bin/python3

import shlex
import socket
import requests
import subprocess

from bs4 import BeautifulSoup


class Cmd:

    def exec_(self, _cmd):
        _cmd = shlex.split(_cmd)
        p = subprocess.Popen(_cmd, stdout=subprocess.PIPE, stdin=subprocess.PIPE, stderr=subprocess.PIPE)
        
        return p.communicate()

    # def exec_poll(self, _cmd, **kwargs):
    #     _cmd = shlex.split(_cmd)
    #     p = subprocess.Popen(_cmd, stdout=subprocess.PIPE, stdin=subprocess.PIPE, stderr=subprocess.PIPE)
        
    #     while p.poll() == None:
    #         out = p.stdout.readline().decode().strip()
    #         yield out

    #     return p.communicate()

    def exec_wait(self, _cmd):
        _cmd = shlex.split(_cmd)
        p = subprocess.Popen(_cmd, stdout=subprocess.PIPE, stdin=subprocess.PIPE, stderr=subprocess.PIPE)
        p.wait()
        return p.communicate()

class Requester:

    _sess = requests.Session()

    @staticmethod
    def get(url, params=None, session=False, **kwargs):
        
        if session:
            r = self._sess.get(url, params=params, **kwargs)
        else:
            r = requests.get(url, params=params, **kwargs)
        return r
    
    @staticmethod
    def post(url, data=None, json=None, session=False, **kwargs):
        if session:
            r = self._sess.get(url, data=data, json=json, **kwargs)
        else:
            r = requests.post(url, data=data, json=json, **kwargs)
        return r

    def check_schema(self, url):
        if url.starswith("http://") or url.startswith("https://"):
            return url
        url = "http://{}".format(url)
        return url

class Misc:
    
    @staticmethod
    def domain2ip(url):
        return socket.gethostbyname(url)

    @staticmethod
    def decode(data):
        if isinstance(data, bytes):
            return data.decode()
        return data

class HtmlParser:

    def __init__(self, raw_html=None):
        # Find a way to init raw_html while using static method
        # so we can can use static method directly without create HtmlParser object
        self._raw_html = raw_html
        self.soup = BeautifulSoup(self._raw_html, 'lxml')
    
    def set_parser(raw_html):
        HtmlParser.__init__()
        self._raw_html = raw_html
        self.soup = BeautifulSoup(self.raw_html, 'lxml')
    
    def getElementsByTagName(self, **kwargs):
        return self.soup.findAll(**kwargs)

    def getElementByTagName(self, **kwargs):
        return self.soup.find(**kwargs)
    
    def get_title(self):
        return self.soup.title.getText()


class File:

    @staticmethod
    def file_get_content(filename):
        return open(filename, "r").read()
    
    def file_put_content(filename, content):
        with open(filename, "w") as f:
            f.write(content)

if __name__ == '__main__':
    # raw_html = Requester.get("http://127.0.0.1", headers={"User-Agent" : "Hello World"}).content
    # t = HtmlParser(raw_html)
    # print(t.getElementsByTagName(name="a", attrs={"rel" : "nofollow"}))
    cmd = Cmd()
    
    # while 1:
    print(cmd.exec_poll("nmap -sV 127.0.0.1"))
    # requests.get("http://127.0.0.1:2121", headers={"User-Agent" : "Hello World"})
