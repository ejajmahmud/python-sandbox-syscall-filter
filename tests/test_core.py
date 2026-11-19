"""Tests for Sandbox Filter."""
import unittest
from python_sandbox_syscall_filter.core import PythonSandboxSyscallFilter, SecurityViolation

class TestPythonSandboxSyscallFilter(unittest.TestCase):
    def test_safe_math(self):
        res = PythonSandboxSyscallFilter.execute_safe("x = sum([1, 2, 3])")
        self.assertEqual(res["x"], 6)

    def test_blocks_os_import(self):
        with self.assertRaises(SecurityViolation):
            PythonSandboxSyscallFilter.execute_safe("import os")
