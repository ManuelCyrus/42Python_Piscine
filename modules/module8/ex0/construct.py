import sys
import os
import site


def in_venv():
    return sys.prefix != sys.base_prefix


def get_venv_name():
    return os.path.basename(sys.prefix)


def get_site_packages():
    if hasattr(site, "getsitepackages"):
        return site.getsitepackages()[0]
    return "unknown"


if in_venv():
    venv_name = get_venv_name()
    print("MATRIX STATUS: Welcome to the construct")
    print(f"Current Python: {sys.executable}")
    print(f"Virtual Environment: {venv_name}")
    print(f"Environment Path: {sys.prefix}")
    print("SUCCESS: You're in an isolated environment!")
    print("Safe to install packages without affecting")
    print("the global system.")
    print()
    print("Package installation path:")
    print(get_site_packages())

else:
    print("MATRIX STATUS: You're still plugged in")
    print(f"Current Python: {sys.executable}")
    print("Virtual Environment: None detected")
    print("WARNING: You're in the global environment!")
    print("The machines can see everything you install.")
    print("To enter the construct, run:")
    print("python -m venv matrix_env")
    print("source matrix_env/bin/activate # On Unix")
    print("matrix_env\\Scripts\\activate # On Windows")
    print("Then run this program again.")
