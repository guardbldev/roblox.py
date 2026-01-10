import sys
from sync import studio_sync, live_sync_opt, test_runner, hash_sort_output
from lint.runner import LintRunner, lint_infinite_yield, lint_event_disconnect
from debug import live_debug_bridge

def build():
    py_files = studio_sync.find_python_files()
    hash_db = {}
    for f in hash_sort_output.stable_files(py_files):
        luau_code, sourcemap = compile_file(f)
        luau_code = hash_sort_output.stable_format_code(luau_code)  # Git-friendly
        output_path = studio_sync.output_path(f)
        hash_sort_output.output_file(output_path, luau_code, hash_db)
        studio_sync.write_sourcemap(f, output_path, sourcemap)

def watch():
    live_sync_opt.sync_files(studio_sync.find_python_files())

def test():
    test_runner.run_test()

def lint():
    runner = LintRunner([lint_infinite_yield, lint_event_disconnect])
    for py_file in studio_sync.find_python_files():
        issues = runner.run(py_file)
        for issue in issues:
            print(f"[Lint] {issue.msg} in {issue.file}:{issue.line}")

def debug():
    dbg = live_debug_bridge.DebugSession()
    dbg.connect()
    # Provide CLI for setting breakpoints, etc.

if __name__ == "__main__":
    cmd = sys.argv[1]
    {"build": build,
     "watch": watch,
     "test": test,
     "lint": lint,
     "debug": debug}[cmd]()