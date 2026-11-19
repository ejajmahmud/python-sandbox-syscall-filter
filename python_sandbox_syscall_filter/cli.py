"""CLI for Sandbox Filter."""
import argparse
from .core import PythonSandboxSyscallFilter, SecurityViolation

def main():
    parser = argparse.ArgumentParser(description="Python Sandbox Syscall Filter CLI")
    parser.add_argument("--demo", action="store_true", help="Run sandbox demo")
    args = parser.parse_args()

    safe_code = """a = 10
b = 20
res = a + b"""
    locals_out = PythonSandboxSyscallFilter.execute_safe(safe_code)
    print(f"Safe code executed: res = {locals_out.get('res')}")

    try:
        PythonSandboxSyscallFilter.execute_safe("import os; os.system('ls')")
    except SecurityViolation as e:
        print(f"Successfully caught security violation: {e}")

if __name__ == "__main__":
    main()
