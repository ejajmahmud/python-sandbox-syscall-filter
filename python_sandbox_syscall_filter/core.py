"""Core Python Sandbox Syscall Filter."""
from typing import Dict, Any, Optional

class SecurityViolation(Exception):
    pass

class PythonSandboxSyscallFilter:
    RESTRICTED_MODULES = {"os", "subprocess", "socket", "sys", "shutil"}

    @classmethod
    def execute_safe(cls, code_str: str, allowed_globals: Optional[Dict[str, Any]] = None) -> Dict[str, Any]:
        safe_globals = allowed_globals or {}
        
        def guarded_import(name, *args, **kwargs):
            if name in cls.RESTRICTED_MODULES:
                raise SecurityViolation(f"Unauthorized import of restricted module: {name}")
            return __import__(name, *args, **kwargs)

        safe_builtins = {
            "__import__": guarded_import,
            "len": len,
            "range": range,
            "min": min,
            "max": max,
            "sum": sum,
            "print": print,
            "int": int,
            "str": str,
            "float": float,
            "list": list,
            "dict": dict,
            "set": set
        }
        safe_globals["__builtins__"] = safe_builtins

        local_vars: Dict[str, Any] = {}
        exec(code_str, safe_globals, local_vars)
        return local_vars
