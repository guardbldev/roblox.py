def emit_remote_permission(node):
    # @remote(allow="admin")
    deco = [d for d in node.decorator_list if getattr(d,"id","")=="remote"]
    perm = None
    if deco and deco[0].args: perm = deco[0].args[0].s
    code = f"if not player:IsInGroup('{perm}') then error('Permission denied') end"
    return code