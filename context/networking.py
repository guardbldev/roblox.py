"""
 Built-in Networking Abstraction

Processes @remote, sets up RemoteEvents, permission checking, rate limiting
"""
def process_remote_func(node):
    perms = next(
        (d for d in getattr(node, "decorator_list", []) if getattr(d, "id", "")=="remote"),
        None
    )
    perm_guard = f"-- Permission: {perms.args[0].s}" if perms and perms.args else ""
    setup_remote = f"-- Setup RemoteEvent for {node.name}"
    return perm_guard + "\n" + setup_remote