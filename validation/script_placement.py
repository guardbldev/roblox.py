"""
Automatic Script Placement System

Routes compiled output into proper folders per context.
"""
def get_script_output_path(decorators, filename):
    # Called for each compiled file
    if 'server_only' in decorators: return f"ServerScriptService/{filename}.lua"
    if 'client_only' in decorators: return f"StarterPlayerScripts/{filename}.lua"
    if 'replicated' in decorators: return f"ReplicatedStorage/{filename}.lua"