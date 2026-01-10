import ast

class LintIssue:
    def __init__(self, msg, file, line):
        self.msg = msg
        self.file = file
        self.line = line

class LintRunner:
    def __init__(self, rules):
        self.rules = rules  # List of lint rule functions
    def run(self, py_file):
        tree = ast.parse(open(py_file).read())
        issues = []
        for rule in self.rules:
            result = rule(tree, py_file)
            issues += result if result else []
        return issues

def lint_infinite_yield(tree, file):
    issues = []
    for n in ast.walk(tree):
        if isinstance(n, ast.While) and not any(isinstance(b, ast.Break) for b in n.body):
            issues.append(LintIssue("Infinite while/yield detected", file, n.lineno))
    return issues

def lint_event_disconnect(tree, file):
    # Warn if event is connected but never disconnected
    issues = []
    for n in ast.walk(tree):
        if isinstance(n, ast.Call) and hasattr(n.func, 'attr') and n.func.attr == "Connect":
            # Traverse for Disconnect calls (not robust in stub)
            if not any(f for f in ast.walk(tree) if getattr(f,"attr",None)=="Disconnect"):
                issues.append(LintIssue("Event connection not disconnected", file, n.lineno))
    return issues