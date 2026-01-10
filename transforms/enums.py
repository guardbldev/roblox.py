def emit_luau_enum(ast_node):
    # expects ClassDef with Enum base; enumerate Assign nodes
    fields = []
    for n in ast_node.body:
        if isinstance(n, ast.Assign):
            fields.append(f"{n.targets[0].id} = {n.value.value}")
    return [f"local {ast_node.name} = {{ {', '.join(fields)} }}"]