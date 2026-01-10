"""
Feature 11. Python Coroutines → task.spawn

Maps async def and await to corresponding task.spawn/task.wait in Luau.
"""
def compile_async_func(node):
    # Detect async def → wrap in task.spawn()
    if getattr(node, "async_function", False):
        body = "...body..."  # compile Python body to Luau
        return f"task.spawn(function()\n{body}\nend)"