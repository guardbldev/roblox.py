from plugin_api import Plugins

class NetworkingPlugin:
    def apply(self, ir_nodes):
        # Find IR nodes marked for networking, apply networking transforms
        for node in ir_nodes:
            if hasattr(node, "networking"):
                node = networking.emit_remote_event(node)
        return ir_nodes

class ECSPlugin:
    def apply(self, ir_nodes):
        # Transform ECS patterns to Luau components/entities
        ...
        return ir_nodes

def load_plugins():
    plugins = Plugins()
    plugins.register(NetworkingPlugin())
    plugins.register(ECSPlugin())
    return plugins