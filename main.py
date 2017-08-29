import os
import sys
import inspect


if len(sys.argv) <= 2:
    exit(0)

submodule = sys.argv[1]
func = sys.argv[2]
try:
    submodule = __import__(submodule)
except ModuleNotFoundError:
    exit(0)


func = getattr(submodule, func, None)
if inspect.isfunction(func):
    func()
