"""
Feature 18. Luau Escape Hatch

Allow inline Luau code blocks via python: lua('...')
"""
def compile_lua_escape(node):
    # Accept lua('...code...') and emit code directly
    if isinstance(node, ast.Call) and getattr(node.func, 'id', '') == 'lua':
        code = node.args[0].s
        return code