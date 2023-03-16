import sys
from datetime import datetime

#Define target
if len(sys.argv) == 2:
    target = socket.gethostbyname(sys.argv[1])
else: 
    print("Invalid amout of arguments")
    print("Syntax: python 3 scan.py <ip address>")
    
#Banner
print("-" *50)
print(f"Scanning target: {target}")
print(f"Time started: {str(datetime.now())}")
print("-" *50)

# Scan for ports between 50 and 445
try:
    for port in range(50,445):
        sox = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        socket.setdefaulttimeout(1)
        result = socket.connect_ex((target,port))
        if result == 0:
            print(f"Port {port} is open @ time: {str(datetime.now())}")
        sox.close
#Errors
except KeyboardInterrupt:
    print("\nExiting program")
except socket.gaierror:
    print("\nHostname could not be resolved")
except socket.error:
    print("Could not connect to server/address")