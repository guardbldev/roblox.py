def optimal_thread(block):
    # Analyze async/coroutines usage to pick: defer/wait/spawn
    if "sleep" in block or "wait" in block: return "task.wait"
    if "async" in block: return "task.spawn"
    # More advanced analysis...
    return "task.defer"
def emit_thread_block(code_block):
    model = optimal_thread(code_block)
    return f"{model}(function()\n{code_block}\nend)"