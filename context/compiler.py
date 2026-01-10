import os, re, hashlib
import ast
from typing import Dict, Optional, Any
from roblox_py.transform import PythonToLuauTransformer
from roblox_py.rojo_sync import RojoSyncManager

class CompilerConfig:
    def __init__(self):
        self.type_check = True
        self.deterministic_hash = True
        self.src_dirs = {
            'server': 'src/server',
            'client': 'src/client',
            'shared': 'src/shared',
        }

class Compiler:
    def __init__(self, config: Optional[CompilerConfig]=None):
        self.config = config or CompilerConfig()
        self.rojo_manager = RojoSyncManager(self.config.src_dirs)

    def build_project(self):
        files = self.rojo_manager.enumerate_files()
        for py_path, service in files.items():
            with open(py_path, "r") as f:
                code = f.read()
            tree = ast.parse(code)
            transformer = PythonToLuauTransformer(service=service)
            luau_code = transformer.transform(tree)
            hashval = hashlib.sha1(luau_code.encode('utf8')).hexdigest()[:6]
            luau_code = f"-- roblox.py hash: {hashval}\n" + luau_code
            self.rojo_manager.write_luau(py_path, luau_code, hashval, service)
        self.rojo_manager.sync_rojo()

    def watch_project(self):
        # Advanced: file watcher that hot-reloads on changes
        self.rojo_manager.watch_sources(self.build_project)