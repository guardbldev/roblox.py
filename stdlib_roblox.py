"""
Feature 3. Roblox-Aware Standard Library

Abstract Python stdlib calls to Roblox APIs in Luau.
"""
STDLIB_MAP = {
    'Players': 'game:GetService("Players")',
    'RunService': 'game:GetService("RunService")',
}

def import_stdlib_module(modname):
    if modname in STDLIB_MAP:
        return f"local {modname} = {STDLIB_MAP[modname]}"
    return None

def resolve_python_stdlib_imports(ast_tree):
    # Scan imports, inject Luau GetService statements
    for node in ast.walk(ast_tree):
        if isinstance(node, ast.ImportFrom) and node.module == "roblox":
            return [import_stdlib_module(name.name) for name in node.names]