class TypeChecker:
    def validate(self, ir_nodes, context):
        for node in ir_nodes:
            if hasattr(node, "args"):
                for a in node.args:
                    # Example error: using DataStoreService on client
                    if a == "DataStoreService" and context=="client":
                        raise TypeError("DataStoreService cannot be used on client context.")
            # More advanced: validate type annotations, API calls