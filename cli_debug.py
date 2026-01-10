def start_debug():
    # No plugin needed: uses socket/source maps for breakpoints
    from sync.source_maps import SourceMap
    import socket
    # Connect to debugger agent, map breakpoints to python code lines
    ...