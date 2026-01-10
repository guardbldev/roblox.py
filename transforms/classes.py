def emit_luau_class(ast_node):
    class_name = ast_node.name
    base = ast_node.bases[0].id if ast_node.bases else None
    body = []
    methods = [n for n in ast_node.body if isinstance(n, ast.FunctionDef)]
    body.append(f"local {class_name} = {{}}")
    body.append(f"{class_name}.__index = {class_name}")
    if base:
        body.append(f"setmetatable({class_name}, {base})")
    for m in methods:
        args = ", ".join(["self"] + [a.arg for a in m.args.args])
        if "classmethod" in [d.id for d in m.decorator_list if isinstance(d, ast.Name)]:
            args = ", ".join([a.arg for a in m.args.args])
        body.append(f"function {class_name}:{m.name}({args})\n    ...\nend")
    body.append(f"function {class_name}.new(...)\n    local self = setmetatable({{}}, {class_name})\n    ...\n    return self\nend")
    return body