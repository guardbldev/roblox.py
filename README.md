# roblox.py

**roblox.py** is a **Python → Luau compiler for Roblox**, designed to let developers write Roblox games using **modern Python syntax** while targeting **typed Luau** and **Rojo-based workflows**. This project started in 2021 by @guardbl and @mikee to break the limits on roblox. Progress may be slow but we are soon to finish the project in 2026. Stay Tuned!!

##  Why roblox.py?

Roblox development today is powerful, but Luau can be limiting for developers coming from other ecosystems. Python is one of the most widely used languages in the world, with a clean syntax and strong tooling. **roblox.py bridges that gap**.
Since the introduction of roblox-ts, we have made several changes so players can easily migrate to our one, one of the examples we use is Rojo. We are NOT in competition with the roblox-ts people, our goal is to make it so that it is easy to use roblox.py.
With roblox.py, you write Python — and deploy Luau Scripts that:

* Run directly in Roblox
* Follow Roblox’s threading and replication rules
* Integrate seamlessly with **Rojo**
* Support **strict typing**, **services**, and **events**

---

## Goals

* **Python-first Roblox development**
* **Zero runtime overhead** (compiled, not interpreted)
* **Rojo-native project structure**
* **Typed Luau output (`--!strict`)**
* **Studio-safe, production-ready code**

---

## How it works

1. You write Roblox code in Python (`.py`)
2. roblox.py parses and analyzes the Python AST
3. Code is compiled into optimized Luau
4. Output is synced into Roblox Studio via **Rojo**

---

## Designed For

* Roblox developers who prefer Python
* Studios using **Rojo**
* Tooling / engine-focused developers
* Large-scale Roblox projects
  etc...

---

## Status

> roblox.py is not completed.
> APIs, syntax support, and features may change rapidly.


