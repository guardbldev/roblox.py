def service_for_path(filepath):
    if "src/server/" in filepath: return "ServerScriptService"
    if "src/client/" in filepath: return "StarterPlayerScripts"
    if "src/shared/" in filepath: return "ReplicatedStorage"
    raise Exception(f"Unknown context for {filepath}")
def output_path(py_path):
    module = os.path.basename(py_path).replace(".py",".lua")
    return f"out/{service_for_path(py_path)}/{module}"