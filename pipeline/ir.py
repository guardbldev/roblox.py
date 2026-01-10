class IRFunction:
    def __init__(self, name, args, body, decorators, context, is_async, lineno):
        self.name = name
        self.args = args
        self.body = body
        self.decorators = decorators
        self.context = context
        self.is_async = is_async
        self.lineno = lineno

class IRTransformer:
    def transform(self, py_ast):
        # Converts Python AST to IR nodes
        # Transforms functions, classes, enums, etc. into IR
        nodes = []
        for node in py_ast.body:
            if isinstance(node, ast.FunctionDef):
                decorators = [d.id for d in node.decorator_list if isinstance(d, ast.Name)]
                nodes.append(IRFunction(
                    node.name,
                    [a.arg for a in node.args.args],
                    node.body,
                    decorators,
                    'server' if 'server_only' in decorators else 'client' if 'client_only' in decorators else 'replicated',
                    hasattr(node, 'async_function'),
                    node.lineno
                ))
            # ... handle classes, enums, etc.
        return nodes