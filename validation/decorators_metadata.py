"""
Feature 4. Decorator-Based Roblox Metadata

Analyze Python decorators on top-level functions/classes,
drive script placement & metadata in Luau.
"""
def get_decorations(func_or_class_node):
    return [
        d.id for d in getattr(func_or_class_node, "decorator_list", [])
        if isinstance(d, ast.Name)
    ]

def route_script(decorators):
    if 'server_only' in decorators:
        return "ServerScriptService"
    if 'client_only' in decorators:
        return "StarterPlayerScripts"
    if 'replicated' in decorators:
        return "ReplicatedStorage"