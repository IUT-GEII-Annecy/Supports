from __future__ import annotations
from pathlib import Path
import shutil
from typing import Optional




def create_root(base: Path, root_name: str, clear: bool = False) -> Path:
    """Create (optionally reset) the root LaTeX output directory.


    Works on Windows/Linux. When clear=True, remove existing dir first.
    """
    root = base / root_name
    if root.exists() and clear:
        shutil.rmtree(root)
    root.mkdir(parents=True, exist_ok=True)
    return root




def write_text(path: Path, content: str, encoding: str = "utf-8") -> None:
    path.parent.mkdir(parents=True, exist_ok=True)
    path.write_text(content, encoding=encoding)




def read_text(path: Path, encoding: str = "utf-8") -> str:
    return path.read_text(encoding=encoding)