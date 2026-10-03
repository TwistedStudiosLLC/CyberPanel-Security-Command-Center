"""Static security-boundary checks over the production modules (DEC-029; DEC-089 D89-16)."""

import ast
import pathlib
import unittest

PKG = pathlib.Path(__file__).resolve().parents[1]
PRODUCTION = sorted(p for p in PKG.glob("*.py"))

FORBIDDEN_MODULES = {
    "subprocess",
    "os",
    "shutil",
    "socket",
    "ssl",
    "http",
    "urllib",
    "requests",
    "asyncio",
    "multiprocessing",
    "ctypes",
    "pty",
    "signal",
    "cbor",
    "cbor2",
    "nacl",
    "cryptography",
    "hmac",
    "secrets",
    "pickle",
    "marshal",
}
FORBIDDEN_CALLS = {
    "exec",
    "eval",
    "compile",
    "open",
    "__import__",
    "system",
    "popen",
    "spawn",
}
FORBIDDEN_WORDS = (
    "ed25519",
    "cbor",
    "cyberpanel",
    "unix_socket",
    "af_unix",
    "job_state",
    "create_job",
)


class BoundaryTests(unittest.TestCase):
    def test_production_modules_present(self):
        self.assertEqual(
            {p.name for p in PRODUCTION},
            {
                "__init__.py",
                "audit.py",
                "core.py",
                "inputs.py",
                "model.py",
                "policy.py",
                "serialization.py",
                "store.py",
            },
        )

    def test_no_forbidden_imports_or_calls(self):
        for path in PRODUCTION:
            tree = ast.parse(path.read_text(encoding="utf-8"))
            for node in ast.walk(tree):
                if isinstance(node, ast.Import):
                    for alias in node.names:
                        self.assertNotIn(
                            alias.name.split(".")[0], FORBIDDEN_MODULES, path.name
                        )
                elif isinstance(node, ast.ImportFrom) and node.level == 0:
                    self.assertNotIn(
                        (node.module or "").split(".")[0], FORBIDDEN_MODULES, path.name
                    )
                elif isinstance(node, ast.Call):
                    fn = node.func
                    name = (
                        fn.id
                        if isinstance(fn, ast.Name)
                        else fn.attr
                        if isinstance(fn, ast.Attribute)
                        else ""
                    )
                    self.assertNotIn(name, FORBIDDEN_CALLS, f"{path.name}: {name}")

    def test_no_excluded_subsystem_vocabulary_in_code(self):
        for path in PRODUCTION:
            tree = ast.parse(path.read_text(encoding="utf-8"))
            names = {n.id.lower() for n in ast.walk(tree) if isinstance(n, ast.Name)}
            names |= {
                n.attr.lower() for n in ast.walk(tree) if isinstance(n, ast.Attribute)
            }
            names |= {
                n.name.lower()
                for n in ast.walk(tree)
                if isinstance(n, (ast.FunctionDef, ast.ClassDef))
            }
            for word in FORBIDDEN_WORDS:
                self.assertFalse(any(word in n for n in names), f"{path.name}: {word}")

    def test_only_sqlite_is_used_for_persistence(self):
        imports = set()
        for path in PRODUCTION:
            for node in ast.walk(ast.parse(path.read_text(encoding="utf-8"))):
                if isinstance(node, ast.Import):
                    imports |= {a.name.split(".")[0] for a in node.names}
                elif isinstance(node, ast.ImportFrom) and node.level == 0:
                    imports.add((node.module or "").split(".")[0])
        self.assertLessEqual(
            imports,
            {
                "__future__",
                "collections",
                "dataclasses",
                "datetime",
                "enum",
                "typing",
                "uuid",
                "json",
                "sqlite3",
                "contextlib",
                "hashlib",
                "math",
            },
        )


if __name__ == "__main__":
    unittest.main()
