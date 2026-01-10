import hashlib
def add_hash_comment(luau_code):
    h = hashlib.sha1(luau_code.encode()).hexdigest()[:6]
    return f"-- roblox.py hash: {h}\n" + luau_code