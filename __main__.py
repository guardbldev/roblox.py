import argparse
import sys
from roblox_py.project import RojoProject
from roblox_py.compiler import Compiler, CompilerConfig
from roblox_py.test_runner import run_tests
from roblox_py.codegen import generate_service_stub
from roblox_py.debugger import Debugger

def main():
    parser = argparse.ArgumentParser(prog='roblox.py', description='Python → Roblox Luau compiler & tooling')
    subparsers = parser.add_subparsers(dest='command')

    sp_init = subparsers.add_parser('init', help='Create new Rojo project')
    sp_test = subparsers.add_parser('test', help='Run tests in Luau VM or Studio')
    sp_build = subparsers.add_parser('build', help='Build and sync to Roblox Studio')
    sp_watch = subparsers.add_parser('watch', help='Watch and auto-sync')
    sp_gen = subparsers.add_parser('gen', help='Generate Python bindings for Roblox service')
    sp_gen.add_argument('service', type=str)
    sp_debug = subparsers.add_parser('debug', help='Attach to Studio debugger')

    args = parser.parse_args()

    if args.command == 'init':
        RojoProject().generate_default()
    elif args.command == 'test':
        run_tests()
    elif args.command == 'build':
        Compiler().build_project()
    elif args.command == 'watch':
        Compiler().watch_project()
    elif args.command == 'gen':
        generate_service_stub(args.service)
    elif args.command == 'debug':
        Debugger().attach()
    else:
        parser.print_help()
        sys.exit(1)

if __name__ == '__main__':
    main()