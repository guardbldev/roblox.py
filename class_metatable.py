"""
Feature 5. Python Classes → Luau Metatables

Convert Python class definitions (init, method types, inheritance) to strict Luau metatables.
"""
def compile_class_metatable(clsnode):
    class_name = clsnode.name
    methods = [n for n in clsnode.body if isinstance(n, ast.FunctionDef)]
    bases = [b.id for b in clsnode.bases]
    luau_ctor = "function {name}:new(...)\n local self = setmetatable({}, {__index = {name}})\n ... \n return self \nend".format(name=class_name)
    # Compile other methods and inheritance by extending metatable
    return luau_ctor + "\n" + "\n".join(f"-- {m.name} method" for m in methods)