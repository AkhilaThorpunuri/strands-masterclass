import sys
from importlib.metadata import PackageNotFoundError, version

import strands


print("Python version:")
print(sys.version)

print("\nStrands Agents installation:")

try:
    strands_version = version("strands-agents")
    print(f"Strands Agents version: {strands_version}")
except PackageNotFoundError:
    print("Strands Agents package was not found.")
    raise

print("\nImport verification:")

from strands import Agent

print("Agent imported successfully.")

print("\nInstallation verified.")
