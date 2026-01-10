"""
Feature 2. Python → Luau Type Mapping

Type translation logic for both code and type annotations.
"""
PY_LUA_TYPE_MAP = {
    'int': 'number',
    'float': 'number',
    'str': 'string',
    'bool': 'boolean',
    'dict': '{[any]: any}',
    'list': '{any}',
}

def python_to_luau_type(py_type, typed_dict_map=None):
    if isinstance(py_type, str):
        return PY_LUA_TYPE_MAP.get(py_type, py_type)
    if hasattr(py_type, '__annotations__'): # TypedDict class
        fields = [
            f"{k}: {python_to_luau_type(v)}"
            for k, v in py_type.__annotations__.items()
        ]
        return f"{{ {', '.join(fields)} }}"
    # expand as needed