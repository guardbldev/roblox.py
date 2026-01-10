import json
import os

class RojoProject:
    DEFAULT_STRUCTURE = {
        'src': {
            'server': {},
            'client': {},
            'shared': {},
        }
    }
    DEFAULT_PROJECT = {
        "name": "roblox.py-project",
        "tree": {
            "$className": "DataModel",
            "ServerScriptService": {"$path": "src/server"},
            "StarterPlayer": {
                "StarterPlayerScripts": {"$path": "src/client"}
            },
            "ReplicatedStorage": {"$path": "src/shared"}
        }
    }

    def generate_default(self):
        os.makedirs("src/server", exist_ok=True)
        os.makedirs("src/client", exist_ok=True)
        os.makedirs("src/shared", exist_ok=True)
        with open("default.project.json", "w") as f:
            json.dump(self.DEFAULT_PROJECT, f, indent=4)
        print("Initialized Roblox project with Rojo mapping.")