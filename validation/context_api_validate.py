CONTEXT_API = {
    "client":["TeleportService", "DataStoreService"],
    "server":["UserInputService"]
}
def validate_api_usage(tree, context):
    for node in ast.walk(tree):
        if isinstance(node, ast.Name) and node.id in CONTEXT_API.get(context, []):
            raise Exception(f"API {node.id} misuse in {context} script.")