import json

with open("stdlib/api_map.json") as f:
    API_MAP = json.load(f)
def resolve_import(name):
    return API_MAP.get(name, None)

def inject_game_service(imported):
    # Returns Luau code for appropriate game:GetService
    for imp in imported:
        code = resolve_import(imp)
        if code:
            yield f"local {imp} = {code}"