
import Pseudosocket
import socket
def gethostName(host: str) - >host:
    host =  input("Host: ").strip()
    while True:
        if host == '':
            print("please specify a host (either a name or an IP address)  ")
            
        else:
            return host
        
def getPort(Port: int)->Port:
    while True:

        try:
        
            Port  = int(input("Port: ")).strip()

            if Port < 0 and Port > 655535:
                print("Please enter the port that is a integer ")
            else:
            
                return Port
            
        except ValueError:
            print("port must be an int between  0 and 65535")

        


