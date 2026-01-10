"""
Feature 9. Roblox Event Syntax Sugar

Maps += Python event bindings to Luau's :Connect
"""
def compile_event_bind(node):
    # e.g. Players.player_added += handler
    lhs = node.targets[0]
    handler = node.value
    if isinstance(lhs, ast.Attribute) and node.op.__class__.__name__ == "Add":
        return f"{lhs.value.id}.{lhs.attr}:Connect({handler.id})"