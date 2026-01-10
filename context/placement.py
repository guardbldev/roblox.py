def get_context_for_file(py_file, py_ast):
    # Returns Roblox service based on content/decorators
    for node in py_ast.body:
        deco = decorators.get_decorators(node)
        if deco:
            return decorators.classify_script(node)
    return "ReplicatedStorage"  # default/fallback