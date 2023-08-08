import socket
import subprocess
import time 
import sys
import pyfiglet 

subprocess.call('clear', shell=True)

Port_Scanner_Banner = pyfiglet.figlet_format("PORT SCANNER")
print(Port_Scanner_Banner)
time.sleep(1)

remoteServer = input("Enter an IP to scan:")
target = socket.gethostbyname(remoteServer)

print("_" * 50)
print("Scanning the following host: " + target)
print("_" * 50)

try:

    for port in range (1, 2048):
        print(f"checking port {port}")
        s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        s.settimeout(.1)
        result = s.connect_ex((target, port))

        if result == 0:
            print(f"Port {port}: is open")

        s.close()

except KeyboardInterrupt:
    print("\n The Scan Was Cancelled")
    sys.exit()

except socket.gaierror:
    print("\n Hostname Could Not Be Resolved")
    sys.exit()

except socket.error:
    print("\n No Response")
    sys.exit()
