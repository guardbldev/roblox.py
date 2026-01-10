import shutil, os
class PackageBundler:
    @staticmethod
    def bundle_packages(source_dir, target_dir):
        # True dependency tree-shake & bundle (stub, minify)
        pkgs = [d for d in os.listdir(source_dir) if os.path.isdir(os.path.join(source_dir,d))]
        for pkg in pkgs:
            src = os.path.join(source_dir, pkg)
            target = os.path.join(target_dir, pkg)
            os.makedirs(target, exist_ok=True)
            # TODO: minification/transpile, dependency analysis
            for file in os.listdir(src):
                if file.endswith(".py"):
                    shutil.copy(os.path.join(src,file), os.path.join(target,file.replace(".py",".lua")))