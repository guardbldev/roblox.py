def gen_service_stub(service_name):
    roblox_api = {
        "Players": ["LocalPlayer","PlayerAdded","GetPlayers"],
        "DataStoreService":["GetDataStore"]
    }
    if service_name not in roblox_api: return
    lines = [f"class {service_name}:"]
    for m in roblox_api[service_name]:
        lines.append(f"    def {m}(self): ... # type: callable")
    open(f"stubs/{service_name}.py","w").write("\n".join(lines))
    print(f"{service_name} stub generated.")