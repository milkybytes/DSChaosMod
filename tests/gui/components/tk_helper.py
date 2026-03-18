"""Shared tkinter root for GUI component tests.

Python 3.14+ changed Tcl's shutdown behaviour so that a Tk instance cannot be
recreated after destroy() is called in the same process.  All test classes must
share this single root and must NOT call destroy() during teardown.
"""

import tkinter as tk

_root = None


def get_root() -> tk.Tk:
    global _root
    if _root is None:
        _root = tk.Tk()
    return _root
