import os, sys

full_path = os.environ.get("PATH")
paths = full_path.split(":")
print(paths)