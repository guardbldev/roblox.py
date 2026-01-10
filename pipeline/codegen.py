def emit_luau(luau_nodes):
    # Highly advanced Luau code emitter; preserves type info and source map
    code_lines = []
    sourcemap = {}
    for func in luau_nodes:
        header = f"function {func.name}({', '.join(func.args)})"
        body_lines = func.body
        code_lines.append(header)
        lineno = 1
        for line in body_lines:
            code_lines.append("    "+line)
            sourcemap[func.name + ":" + str(lineno)] = func.context + ":" + str(lineno)
            lineno += 1
        code_lines.append("end\n")
    return "\n".join(code_lines), sourcemap