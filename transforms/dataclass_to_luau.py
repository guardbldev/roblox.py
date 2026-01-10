def emit_dataclass(node):
    name = node.name
    fields = [f"{f.arg}: {TYPE_MAP.get(f.annotation.id,'any')}" for f in node.body if isinstance(f,ast.AnnAssign)]
    struct = f"local {name} = {{ __fields = {{ {', '.join(fields)} }} }}"
    struct += f"\nfunction {name}.new(init)\n    local self = {{}}\n    for k,v in pairs({name}.__fields) do self[k] = init[k] or nil end\n    return self\nend"
    return struct