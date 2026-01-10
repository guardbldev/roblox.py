import os

class RojoSyncManager:
    def __init__(self, src_dirs):
        self.src_dirs = src_dirs
        self.out_dirs = {
            'server': 'out/ServerScriptService',
            'client': 'out/StarterPlayerScripts',
            'shared': 'out/ReplicatedStorage',
        }

    def enumerate_files(self):
        mapping = {}
        for typ, path in self.src_dirs.items():
            for fname in os.listdir(path):
                if fname.endswith(".py"):
                    mapping[os.path.join(path, fname)] = typ
        return mapping

    def write_luau(self, py_path, luau_code, hashval, service):
        luau_fname = os.path.basename(py_path).replace(".py", ".lua")
        out_dir = self.out_dirs[service]
        os.makedirs(out_dir, exist_ok=True)
        with open(os.path.join(out_dir, luau_fname), "w") as f:
            f.write(luau_code)

    def sync_rojo(self):
        # Optimized: stable file ordering, skip unchanged
        pass

    def watch_sources(self, rebuild):
        # File watcher: onchange, call rebuild
        pass