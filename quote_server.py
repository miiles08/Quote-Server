"""A server that responds to network connections by sending a random quote"""

import random
import socket

QUOTES = ["Hello","Every dog has it's day","An apple a day"]
SERVER_NAME = "Miles's Server"
PORT = 27526 # Pick something between 10000 and 60000

s = socket.socket() # an instance of the socket class
s.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
s.bind(("0.0.0.0",PORT)) # Asks the OS to create a socket on this PC
s.listen() # Wait for data to come across socket
print(f"Server started on port {PORT}")

while True: # We'll kill our app with CTRL+C
    conn, addr = s.accept()
    quote = random.choice(QUOTES)
    print(f"Sending a random message to {addr[0]}")
    conn.send(quote.encode())
    conn.close()