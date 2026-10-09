# Installation

> Venkata Bhattaram (c) 2026

## Contents

- Installing Strands Agents
- Creating a Python virtual environment
- Installing dependencies
- Verifying the installation
- Running the first Strands Agent
- Installation checklist
- Troubleshooting common issues

## Overview

This Masterclass uses a shared Python environment for all lessons. The environment is configured once and reused throughout the tutorial.

The installation consists of:

- **Python 3.13** — the recommended Python version for this Masterclass.
- **Strands Agents SDK** — the core framework for building AI agents.
- **Virtual Environment** — isolates project dependencies inside `.venv`.
- **Requirements File** — records the packages needed to reproduce the environment.
- **Model Provider** — connects the agent to an LLM when executing model requests.

## 1. Check the Python Version

Check the Python versions installed on your machine:

```powershell
py --list
```

Check the active Python interpreter:

```powershell
python --version
```

For this Masterclass, Python 3.13 is the recommended baseline.

If Python 3.13 is installed, select it explicitly when creating the virtual environment.

## 2. Create a Virtual Environment

Open PowerShell in the root directory of the repository:

Create the virtual environment:

```powershell
py -3.13 -m venv .venv
```

Activate it:

```powershell
.\.venv\Scripts\Activate.ps1
```

Upgrade pip:

```powershell
python -m pip install --upgrade pip
```

Verify the active interpreter:

```powershell
python --version
```

The terminal should display the `(.venv)` prefix when the virtual environment is active.

## 3. Install Strands Agents

Install the core SDK:

```powershell
python -m pip install strands-agents
```

Verify the installed package:

```powershell
python -m pip show strands-agents
```

The output should contain the package name, installed version, and installation location.

For this repository, the verified Strands Agents version is `1.59.0`.

## 4. Configure Dependencies

Create a `requirements.txt` file in the repository root:

```text
strands-agents
```

This records the SDK version used by the verified setup.

Install the dependencies:

```powershell
python -m pip install -r requirements.txt
```

Pinning the SDK version helps keep the course environment consistent. If a future course update intentionally changes the SDK version, update this file and retest the examples.

## 5. Verify the Installation

Create the following file:

```text
01-get-started/code/verify_installation.py
```

Add this code:

```python
import sys
from importlib.metadata import version

from strands import Agent


print("Python version:")
print(sys.version)

print("\nStrands Agents installation:")
print(f"Strands Agents version: {version('strands-agents')}")

print("\nImport verification:")
print("Agent imported successfully.")

print("\nInstallation verified.")
```

Run the script from the repository root:

Expected output:

```text
Python version:
3.13.2 ...

Strands Agents installation:
Strands Agents version: 1.59.0

Import verification:
Agent imported successfully.

Installation verified.
```

## 7. Installation Checklist

Before proceeding to the next lesson, verify the following:

```text
[ ] Python 3.13 installed
[ ] Virtual environment created
[ ] Virtual environment activated
[ ] pip upgraded
[ ] Strands Agents installed
[ ] requirements.txt configured
[ ] Agent import verified
[ ] Installation verification completed
[ ] Model provider configured before executing first_agent.py
```
## Conclusion

The installation process for this Masterclass is:

```text
Python 3.13
     ↓
Virtual Environment
     ↓
Strands Agents SDK
     ↓
Dependency Configuration
     ↓
Installation Verification
     ↓
Model Provider Configuration
     ↓
First Strands Agent
```

The core installation is complete when `verify_installation.py` prints:

```text
Installation verified.
```

The next lesson introduces the fundamental building block of Strands Agents: **creating and understanding an Agent**.