"""
Feature 15. Source Maps (Python ↔ Luau)

Maps Python lines to Luau lines for error mapping and debugging.
"""
class SourceMap:
    def __init__(self):
        self.py_to_luau = {}  # {py_line: luau_line}

    def record(self, py_line, luau_line):
        self.py_to_luau[py_line] = luau_line

    def lookup(self, luau_line):
        # Find which .py line corresponds to this Luau line
        for py, l in self.py_to_luau.items():
            if l == luau_line: return py
        return None