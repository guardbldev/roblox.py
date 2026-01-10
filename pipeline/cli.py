import sys
from pipeline.ast_parse import parse_python_ast
from pipeline.ir import IRTransformer
from pipeline.luau_ast import LuauTransformer
from pipeline.codegen import emit_luau
from context.placement import get_context_for_file
from sync.studio_sync import StudioSync
from sync.hot_reload import HotReloader
from context.type_check import TypeChecker

def compile_file(py_file, out_dir):
    py_ast = parse_python_ast(open(py_file).read())
    ir = IRTransformer().transform(py_ast)
    luau_ast = LuauTransformer().transform(ir)
    luau_code, sourcemap = emit_luau(luau_ast)
    context = get_context_for_file(py_file, py_ast)
    StudioSync.write_luau(py_file, context, luau_code)
    StudioSync.write_sourcemap(py_file, context, sourcemap)
    TypeChecker().validate(ir, context)

def main():
    cmd = sys.argv[1]
    if cmd == "build":
        for py_file in StudioSync.find_python_files():
            compile_file(py_file, "out/")
    elif cmd == "watch":
        HotReloader().start()
    else:
        print("Unknown command.")

if __name__ == "__main__":
    main()