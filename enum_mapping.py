"""
Feature 6. Python Enums → Luau Tables

Turns Python enums into literal Luau tables
"""
def compile_enum(node):
    name = node.name
    members = {
        n.targets[0].id: n.value.value
        for n in node.body if isinstance(n, ast.Assign)
    }
    fields = ", ".join(f"{k} = {v}" for k, v in members.items())
    return f"local {name} = {{ {fields} }}"