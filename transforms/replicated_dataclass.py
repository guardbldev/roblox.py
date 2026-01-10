def emit_replication_struct(class_node):
    name = class_node.name
    code = [emit_dataclass(class_node)]
    code.append(f"-- Replicated: delta compression sync for {name}")
    code.append(f"function {name}:SyncDelta(other) ... end")
    return "\n".join(code)