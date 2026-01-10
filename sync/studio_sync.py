import os
class StudioSync:
    @staticmethod
    def find_python_files():
        for root, dirs, files in os.walk("src/"):
            for f in files:
                if f.endswith(".py"): yield os.path.join(root, f)
    @staticmethod
    def write_luau(py_file, context, luau_code):
        target = os.path.join("out/", context, os.path.basename(py_file).replace(".py",".lua"))
        os.makedirs(os.path.dirname(target), exist_ok=True)
        with open(target, "w") as f: f.write(luau_code)
    @staticmethod
    def write_sourcemap(py_file, context, sourcemap):
        target = os.path.join("out/", context, os.path.basename(py_file).replace(".py",".map"))
        with open(target, "w") as f: f.write(str(sourcemap))