class TransformPlugin:
    def __init__(self, name):
        self.name = name
    def apply(self, ir_nodes):
        # Transform IR nodes as needed
        return ir_nodes

class Plugins:
    def __init__(self):
        self.plugins = []
    def register(self, plugin:TransformPlugin):
        self.plugins.append(plugin)
    def apply_all(self, ir_nodes):
        for plugin in self.plugins:
            ir_nodes = plugin.apply(ir_nodes)
        return ir_nodes

# Example plugin: Adds ECS support
class ECSPlugin(TransformPlugin):
    def apply(self, ir_nodes):
        # Find ECS components, auto-emit Luau component tables
        return ir_nodes

# Usage:
# plugins = Plugins()
# plugins.register(ECSPlugin("ecs"))
# ir_nodes = plugins.apply_all(ir_nodes)