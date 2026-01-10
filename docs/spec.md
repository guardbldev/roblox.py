# roblox.py: Advanced Python → Roblox Compiler (Luau/Studio Toolchain)

## Features Covered

- Autogen Rojo project (`init`)
- Service-aware Python module mapping
- Python file splitting (`.server/.client` / conditional blocks)
- Rojo live sync, deterministic build, hashing
- Pattern matching, dataclasses, resources, properties, constants
- Service injection (`game:GetService`)
- API misuse validation (Datastore, Teleport, etc.)
- Secure permission system for remotes
- Replication, threading, optimal coroutine mapping
- Test runner, lint rules, API stubs/gen, debugger, sourcemaps, minimal diffs
- Compiler pipeline (AST → IR → Luau AST)
- Robust type mapping (`TypedDict`, Luau types)
- Python stdlib → Roblox API
- Decorator-based metadata & placement system
- Enums, try/except → pcall
- Script placement per context
- Event syntax sugar (`+=`, generator `for _ in`)
- Coroutines, networking abstraction, static type checker
- Studio sync, package/module bundling, hot reload, escape hatch
- Hybrid projects, plugin API