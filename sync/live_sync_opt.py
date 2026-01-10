import time, os
from pipeline import compile_file

def sync_files(files):
    hashes = {}
    while True:
        for f in files:
            code = open(f).read()
            h = file_hash(code)
            if hashes.get(f) != h:
                print("[HotReload] Updating", f)
                luau_code, sourcemap = compile_file(code, f)
                output_path = output_path_from_py(f)
                output_file(output_path, luau_code, hashes)
                # Attach to Studio via Rojo socket/Studio debugger here
                hashes[f] = h
        time.sleep(1)