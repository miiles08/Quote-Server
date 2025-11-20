"""A server that responds to network connections by sending a random quote"""

import random
import socket

QUOTES = ["Hello","Every dog has it's day","An apple a day"]
SERVER_NAME = "Miles's Server"
PORT = 27526 # Pick something between 10000 and 60000