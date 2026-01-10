"""
Feature 20. Plugin API for Custom Transforms

Allow users to plug in AST transforms, decorators, syntax extensions.
"""
class PluginManager:
    def __init__(self):
        self.plugins = []

    def register(self, plugin):
        self.plugins.append(plugin)

    def apply_plugins(self, ast_tree):
        for plugin in self.plugins:
            ast_tree = plugin.transform(ast_tree)
        return ast_tree