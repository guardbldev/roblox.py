import subprocess

def run_test(mode="vm"):
    test_dir = "tests/"
    luau_files = [f for f in os.listdir(test_dir) if f.endswith(".lua")]
    if mode=="vm":
        for f in luau_files:
            subprocess.run(["luau-vm", os.path.join(test_dir,f)])
    elif mode=="studio":
        for f in luau_files:
            subprocess.run(["rojo", "serve", "--load", os.path.join(test_dir,f)])