def compile_match(node):
    # Python ast.Match → Luau if / elseif chain
    subject = node.subject.id
    out = []
    for i, case in enumerate(node.cases):
        val = case.pattern.value.s
        body = [emit_luau(stmt) for stmt in case.body]
        if i == 0:
            out.append(f"if {subject} == '{val}' then")
        else:
            out.append(f"elseif {subject} == '{val}' then")
        out += ["    "+b for b in body]
    out.append("end")
    return out