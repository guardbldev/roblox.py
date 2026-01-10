import ast

class NetworkingIR:
    def __init__(self, name, allow, node):
        self.name = name
        self.allow = allow
        self.node = node  # The original AST node

def parse_remote_functions(tree):
    remotes = []
    for node in ast.walk(tree):
        if isinstance(node, ast.FunctionDef):
            for deco in node.decorator_list:
                if hasattr(deco, "id") and deco.id == "remote":
                    allow = None
                    if getattr(deco, "args", None):
                        allow = deco.args[0].s
                    remotes.append(NetworkingIR(node.name, allow, node))
    return remotes

def emit_remote_event(remote):
    # Build Luau code for RemoteEvents with permissions, rate limiting, context checks
    lines = [
        f"local {remote.name}Event = Instance.new('RemoteEvent')",
        f"{remote.name}Event.Name = '{remote.name}Event'",
    ]
    handler_args = ','.join(a.arg for a in remote.node.args.args)
    lines.append(f"{remote.name}Event.OnServerEvent:Connect(function(player, {handler_args})")
    # Security: permission guard
    if remote.allow:
        lines.append(f"    if not player:IsInGroup('{remote.allow}') then error('Forbidden') end")
    # Rate limiting stub (expand for real implementation)
    lines.append(f"    -- TODO: Rate limiting")
    # User function body
    for stmt in remote.node.body:
        lines.append(f"    {emit_luau(stmt)}")
    lines.append("end)")
    return '\n'.join(lines)