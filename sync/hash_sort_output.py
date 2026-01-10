import hashlib, os

def file_hash(contents): return hashlib.sha1(contents.encode()).hexdigest()[:6]
def stable_files(files): return sorted(files, key=os.path.basename)

def should_output_update(file_path, contents, hash_db):
    h = file_hash(contents)
    previous = hash_db.get(file_path)
    return h != previous

def output_file(file_path, contents, hash_db):
    if should_output_update(file_path, contents, hash_db):
        with open(file_path, "w") as f: f.write(contents)
        hash_db[file_path] = file_hash(contents)

def stable_format_code(luau_code):
    lines = luau_code.strip().splitlines()
    # Alphabetically sort top-level functions (no temp)
    funcs = sorted([l for l in lines if l.startswith("function")])
    other = [l for l in lines if not l.startswith("function")]
    return "\n".join(funcs+other)