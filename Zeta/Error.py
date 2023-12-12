import sys

class Handler:
    def write(self, msg):
        pass

def handle_error():
	sys.stderr = Handler()