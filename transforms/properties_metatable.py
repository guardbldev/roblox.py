def emit_property(class_node):
    # For each @property, emit __index handler
    prop_methods = {}
    for func in class_node.body:
        if hasattr(func, 'decorator_list'):
            for d in func.decorator_list:
                if getattr(d, "id", "") == "property":
                    prop_methods[func.name] = func
    name = class_node.name
    code = [f"{name}.__index = function(self, key)\n    if key == '{func.name}' then return self:{func.name}() end\n    return rawget(self, key)\nend" for func in prop_methods.values()]
    return "\n".join(code)