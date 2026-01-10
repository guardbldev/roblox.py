"""
Feature 10. Roblox Signals as Python Generators

Transforms `for x in Events:` to Luau event connection and loop.
"""
def compile_signal_generator(for_node):
    signal = for_node.iter.attr
    var = for_node.target.id
    body = "...body..."  # expand with real body
    return f"{signal}:Connect(function({var})\n    {body}\nend)"