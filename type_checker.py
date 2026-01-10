"""
Feature 13. Static Type Checker (mypy-style for Roblox)

Analysis pass: validates types, detects misuse of server/client context and APIs
"""
class TypeChecker:
    def check(self, py_tree):
        errors = []
        # Walk AST, check annotations vs Roblox APIs
        for node in ast.walk(py_tree):
            ...
        return errors