import socket
import sys

class PortScanner:
  def __init__(self, host):
    self.host = host
  def __port_scan(self, port):
    server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

    if server.connect_ex((self.host, port)):
      return False
    else: 
      return True
    server.close()
  def port_scan_many(self, port_str: str):
    ports = port_str.split("-")
    for port in range(int(ports[0]), int(ports[1])+1):
      if self.__port_scan(port):
        print(f'{self.host}:{port} open.')

  def port_scan(self, port):
    if self.__port_scan(port):
      print(f'{self.host}:{port} open.')
    else: 
      print(f'{self.host}:{port} closed.')


if sys.argv[1] == "-m":
  scanner = PortScanner(sys.argv[2])
  scanner.port_scan_many(sys.argv[3])
else: 
  scanner = PortScanner(sys.argv[1])
  scanner.port_scan(int(sys.argv[2]))
