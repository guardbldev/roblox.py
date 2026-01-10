from sync.studio_sync import StudioSync
import time
import os

class HotReloader:
    def start(self):
        last_mtime = {}
        while True:
            for f in StudioSync.find_python_files():
                mtime = os.path.getmtime(f)
                if f not in last_mtime or last_mtime[f] != mtime:
                    print("Reloading", f)
                    # Re-compile and sync (could use socket attach for Studio push)
                    compile_file(f, "out/")
                    last_mtime[f] = mtime
            time.sleep(1)