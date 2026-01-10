import json, os

DEFAULT_PROJECT = {
    "name": "roblox.py-project",
    "tree": {
        "$className": "DataModel",
        "ServerScriptService": {"$path": "src/server"},
        "StarterPlayer": {"StarterPlayerScripts": {"$path": "src/client"}},
        "ReplicatedStorage": {"$path": "src/shared"}
    }
}
def run_project_init():
    for d in ["src/server", "src/client", "src/shared"]:
        os.makedirs(d, exist_ok=True)
    with open("default.project.json","w") as f:
        json.dump(DEFAULT_PROJECT, f, indent=4)
    print("Project initialized. Structure mapped to Rojo services.")