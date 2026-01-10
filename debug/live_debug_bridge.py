import socket
import threading
from sync.source_maps import SourceMap

class DebugSession:
    def __init__(self, studio_host="127.0.0.1", port=17897):
        self.studio_host = studio_host
        self.port = port
        self.sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        self.source_map = SourceMap()
        self.breakpoints = {}

    def connect(self):
        self.sock.connect((self.studio_host, self.port))
        threading.Thread(target=self.listen, daemon=True).start()

    def set_breakpoint(self, py_file, py_line):
        lua_line = self.source_map.to_lua(py_file, py_line)
        self.breakpoints[(py_file, py_line)] = lua_line
        # Send to Studio debug agent
        self.sock.send(f"SET_BREAKPOINT:{lua_line}".encode())

    def listen(self):
        while True:
            msg = self.sock.recv(1024).decode()
            if "BREAK" in msg:
                lua_line = int(msg.split(":")[1])
                py_file, py_line = self.source_map.from_lua(lua_line)
                print(f"[Debug] Hit breakpoint at {py_file}:{py_line}")

# Usage
# debug = DebugSession()
# debug.connect()
# debug.set_breakpoint("player.py", 42)