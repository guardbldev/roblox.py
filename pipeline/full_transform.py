from transforms.pattern_matching import compile_match
from transforms.dataclass_to_luau import emit_dataclass
from transforms.with_resource_guard import emit_with
from transforms.properties_metatable import emit_property
from transforms.constant_folding import constant_fold_pass

def transform_ast(ast_tree, plugins):
    # Apply built-in and custom plugins
    constant_fold_pass(ast_tree)
    for node in ast_tree.body:
        if isinstance(node, ast.Match):
            luau_code = compile_match(node)
        elif hasattr(node, "decorator_list") and "dataclass" in [d.id for d in node.decorator_list if hasattr(d,'id')]:
            luau_code = emit_dataclass(node)
        elif isinstance(node, ast.With):
            luau_code = emit_with(node)
        elif hasattr(node, "decorator_list") and "property" in [d.id for d in node.decorator_list if hasattr(d,'id')]:
            luau_code = emit_property(node)
        # ...and so on for all language features
        # Now, apply all custom plugin transforms
    ast_tree = plugins.apply_all(ast_tree)
    return ast_tree