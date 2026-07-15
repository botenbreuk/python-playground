"""Scans the current directory, including subfolders, for .py files and
runs every function decorated with @runnable.

This mirrors how Java frameworks find @Test-annotated methods via
reflection, with one key difference: Python has to execute a module
top-to-bottom before it can see what's inside it, so importing a file
here also runs all of that file's top-level code - not just the
decorated functions. Keep files that get scanned limited to
function/class definitions (guard any script-style code behind
`if __name__ == "__main__":`).
"""

from __future__ import annotations
from pathlib import Path
from utils.logger import log

import importlib.util
import inspect
import sys
import types

_MARKER = "__example__"
_DISABLED_MARKER = "__example_disabled__"
_NAME_MARKER = "__example_name__"


def example(func=None, *, disable=False, name=None):
    """Marks a function so the scanner will pick it up and call it.

    Usable as @example or @example(disable=True). A disabled example
    stays marked but is skipped by the scanner instead of being run.
    """
    def decorator(f):
        setattr(f, _MARKER, True)
        setattr(f, _DISABLED_MARKER, disable)
        log.info("----------------------------------------------------")
        log.info("- Example: {}".format(name if name is not None else f.__name__))
        log.info("----------------------------------------------------")
        return f

    if func is not None:
        return decorator(func)
    return decorator


def _module_name(path: Path, scan_dir: Path) -> str:
    rel = path.relative_to(scan_dir).with_suffix("")
    return ".".join(rel.parts)


def _load_module(path: Path, scan_dir: Path) -> types.ModuleType:
    parent = str(path.parent)
    if parent not in sys.path:
        sys.path.insert(0, parent)

    name = _module_name(path, scan_dir)
    spec = importlib.util.spec_from_file_location(name, path)
    module = importlib.util.module_from_spec(spec)
    sys.modules[name] = module
    spec.loader.exec_module(module)
    return module


def _find_runnables(module: types.ModuleType):
    for _, func in inspect.getmembers(module, inspect.isfunction):
        if getattr(func, _MARKER, False):
            yield func


def _takes_required_args(func) -> bool:
    params = inspect.signature(func).parameters.values()
    return any(
        p.kind in (p.POSITIONAL_ONLY, p.POSITIONAL_OR_KEYWORD)
        and p.default is inspect.Parameter.empty
        for p in params
    )


def _is_hidden(path: Path, scan_dir: Path) -> bool:
    return any(
        part.startswith(".") or part == "__pycache__"
        for part in path.relative_to(scan_dir).parts
    )


def main() -> None:
    scan_dir = Path(__file__).resolve().parent
    self_path = Path(__file__).resolve()

    py_files = sorted(
        path
        for path in scan_dir.rglob("*.py")
        if path.resolve() != self_path
        and not path.name.startswith("_")
        and not _is_hidden(path, scan_dir)
    )

    if not py_files:
        log.info(f"No .py files found in {scan_dir}")
        return

    for path in py_files:
        rel_path = path.relative_to(scan_dir)
        try:
            module = _load_module(path, scan_dir)
        except Exception as exc:
            log.warning(f"[SKIP]  {rel_path}: import failed ({exc!r})")
            continue

        for func in _find_runnables(module):
            if getattr(func, _DISABLED_MARKER, False):
                log.info(f"[SKIP]  {rel_path}:{func.__name__} disabled")
                continue
            if _takes_required_args(func):
                log.info(
                    f"[SKIP]  {rel_path}:{func.__name__} needs arguments, can't auto-run"
                )
                continue
            log.info(f"[RUN]   {rel_path}:{func.__name__}")
            try:
                func()
            except Exception as exc:
                log.error(f"[ERROR] {rel_path}:{func.__name__} raised {exc!r}")


if __name__ == "__main__":
    main()
