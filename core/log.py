import sys
import logging

# import coloredlogs

# logging.basicConfig() 
 
class Log:

    # @staticmethod
    def _print(message):
        sys.stdout.write(message + "\n")
        sys.stdout.flush()

    # @staticmethod
    def info(message):
        Log._print("[+] {}".format(message))
    
    # @staticmethod
    def warning(message):
        Log._print("[!] {}".format(message))
    
    # @staticmethod
    def error(message):
        Log._print("[*] {}".format(message))

if __name__ == '__main__':
    Log.info("HELLO WORLD")
