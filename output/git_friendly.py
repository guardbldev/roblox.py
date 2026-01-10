def stable_format(luau_code):
    # No temp vars, stable indent, sort functions alphabetically
    lines = luau_code.strip().split("\n")
    funcs = [l for l in lines if l.startswith("function")]
    other = [l for l in lines if not l.startswith("function")]
    sorted_code = sorted(funcs) + other
    return "\n".join(sorted_code)