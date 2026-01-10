"""
Feature 14. Roblox Studio Sync Tool

CLI: 'build', 'watch' – incremental sync Luau output to .rbxlx or Rojo folder.
"""
class StudioSync:
    def sync(self, files):
        # Incrementally copy files + trigger Rojo/Studio reload (deterministic sort/order)
        pass
    def watch(self, cb):
        # Watch filesystem and call cb() on change
        pass