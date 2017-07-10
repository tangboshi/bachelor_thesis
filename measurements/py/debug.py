import platform
import sys
import os
import socket

class debug:
    def show_info:
        print(platform.uname())
        print("Python Version: "+sys.version)
        print("IP: "+socket.gethostbyname(socket.gethostname()))
