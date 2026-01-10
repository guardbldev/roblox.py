def transform_try_except(ast_node):
    # Robustly convert Python try/except to Luau pcall
    try_block = ast_node.body
    except_handlers = ast_node.handlers
    result = ["local ok, result = pcall(function()"]
    for stmt in try_block:
        result.append("    "+emit_luau(stmt))
    result.append("end)")
    for handler in except_handlers:
        if handler.type:
            result.append(f"if not ok and result == '{handler.type.id}' then")
        else:
            result.append("if not ok then")
        for hstmt in handler.body:
            result.append("    "+emit_luau(hstmt))
    return result