import socket
import select

import threading
import time

class V2XDataClient:
    def __init__(self):
        self.list = []
        self.sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
        self.sock.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
        self.sock.bind(('',5002))
        self.readable = [self.sock] # list of readable sockets. self.sock is readable if a client is waiting.
  
    def __enter__(self):
        return self

    def __exit__(self, exc_type, exc_val, exc_tb):
        self.sock.close()

    def get_sock_data(self, timeout=10):
        t = time.time() + timeout
        while time.time() < t:
            # r will be a list of sockets with readable data
            data = ""
            r, _, _ = select.select(self.readable,[],[],0)
            for rs in r: # iterate through readable sockets
                # read from a client
                data = rs.recv(1024)
                self.list.append(data)
                return

    def get_items(self):
        return self.list
    
si = V2XDataClient()
with si as s:
    p = threading.Thread(target=si.get_sock_data, args=(0.5,))
    p.start()

    print("TODO: some code here:", p.getName(), "has just started")

    #while p.is_alive():
    #    pass
    
    p.join()

    if si.get_items():
        print(si.get_items()[0].decode("utf-8"))
    else:
        print("No Data")
    
