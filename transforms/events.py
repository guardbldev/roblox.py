def emit_signal_generator(ast_node):
    # for player in Players.player_added:
    if isinstance(ast_node, ast.For):
        if isinstance(ast_node.iter, ast.Attribute):
            obj = ast_node.iter.value.id
            event = ast_node.iter.attr.replace("_", "").title()
            target = ast_node.target.id
            body = [emit_luau(stmt) for stmt in ast_node.body]
            return [f"{obj}.{event}:Connect(function({target})"] + ["    "+b for b in body] + ["end)"]