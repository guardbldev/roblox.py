def get_decorators(ast_node):
    return [
        d.id for d in getattr(ast_node, "decorator_list", [])
        if isinstance(d, ast.Name)
    ]

def classify_script(ast_node):
    deco = get_decorators(ast_node)
    if "server_only" in deco: return "ServerScriptService"
    if "client_only" in deco: return "StarterPlayerScripts"
    if "replicated" in deco: return "ReplicatedStorage"