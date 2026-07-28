import sys
import os
print(f"File: {__file__}")
print(f"Abspath: {os.path.abspath(__file__)}")
print(f"Dirname: {os.path.dirname(os.path.abspath(__file__))}")
print(f"Dirname Dirname: {os.path.dirname(os.path.dirname(os.path.abspath(__file__)))}")
sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
print("sys.path modified")
try:
    from Pages.P02_SignIn import SignIn
    print("Import successful")
except ModuleNotFoundError as e:
    print(f"Import failed: {e}")
    print("sys.path contains:")
    for p in sys.path:
        print(f"  {p}")
