class SourceMap:
    def __init__(self):
        self.py_to_lua = {}   # (py_file, py_line) -> (lua_file, lua_line)
        self.lua_to_py = {}   # (lua_file, lua_line) -> (py_file, py_line)
    def add_map(self, py_file, py_line, lua_file, lua_line):
        self.py_to_lua[(py_file, py_line)] = (lua_file, lua_line)
        self.lua_to_py[(lua_file, lua_line)] = (py_file, py_line)
    def to_lua(self, py_file, py_line):
        return self.py_to_lua.get((py_file, py_line), None)
    def from_lua(self, lua_file, lua_line):
        return self.lua_to_py.get((lua_file, lua_line), None)
    def report_error(self, lua_file, lua_line, msg):
        py = self.from_lua(lua_file, lua_line)
        if py:
            py_file, py_line = py
            print(f"[Error] {msg} at {py_file}:{py_line}")
        else:
            print(f"[Error] {msg} at {lua_file}:{lua_line}")