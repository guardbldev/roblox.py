def inject_services_in_func(node):
    # def f(players:Players, run:RunService): ...
    code = []
    for arg in node.args.args:
        if hasattr(arg,'annotation'):
            service = arg.annotation.id
            code.append(f"local {arg.arg} = game:GetService('{service}')")
    return code