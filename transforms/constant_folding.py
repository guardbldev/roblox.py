import ast
def fold_constants(node):
    if isinstance(node.value, ast.BinOp):
        try: val = eval(compile(ast.Expression(node.value),'<const>','eval'))
        except: val = None
        node.value = ast.Constant(val)
def constant_fold_pass(tree):
    for node in ast.walk(tree):
        if isinstance(node, ast.Assign): fold_constants(node)