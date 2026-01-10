TYPE_MAP = {
    "int":"number",
    "float":"number",
    "str":"string",
    "bool":"boolean",
    "dict":"{[any]: any}",
    "list":"{any}",
    # Extend for TypedDict
}

def map_python_type(py_type):
    # String, ast node, or class: resolves to Luau type
    if isinstance(py_type, str): return TYPE_MAP.get(py_type, py_type)
    if hasattr(py_type, '__annotations__'):  # TypedDict Class
        return "{ " + ", ".join(
            f"{field}: {map_python_type(tp)}"
            for field, tp in py_type.__annotations__.items()
        ) + " }"
    # Extend as needed