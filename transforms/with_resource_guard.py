def emit_with(node):
    mgr = emit_luau(node.items[0].context_expr)
    body = "\n".join(emit_luau(stmt) for stmt in node.body)
    return f"local ok, err = pcall(function()\n{body}\nend)\nif mgr and mgr.cleanup then mgr:cleanup() end"