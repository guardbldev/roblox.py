import ast
from roblox_py.ast_patterns import compile_match, compile_dataclass, compile_with, compile_properties, constant_fold
from roblox_py.roblox_api_inject import inject_services, validate_context_apis
from roblox_py.remote_system import process_remotes

class PythonToLuauTransformer(ast.NodeTransformer):
    def __init__(self, service):
        super().__init__()
        self.service = service

    def transform(self, tree):
        # Advanced multi-pass pipeline
        inject_services(tree)
        validate_context_apis(tree, self.service)
        process_remotes(tree)
        constant_fold(tree)
        luau = []
        for node in tree.body:
            luau.append(self.visit(node))
        return "\n".join(luau)

    def visit_ClassDef(self, node):
        # Dataclass, Replicated, Properties, Enums, Metatables
        if 'dataclass' in [d.id for d in node.decorator_list if isinstance(d, ast.Name)]:
            return compile_dataclass(node)
        # TODO: More compile rules
        return "<Class compilation>"

    def visit_With(self, node):
        return compile_with(node)

    def visit_Match(self, node):
        return compile_match(node)

    def visit_FunctionDef(self, node):
        # Handle @remote, @server_only, service injection, etc.
        return f"<Function compilation: {node.name}>"

    def visit_Module(self, node):
        return "\n".join([self.visit(stmt) for stmt in node.body])