import sys
import os
# No sys.path modification
try:
    from P02_SignIn import SignIn
    print("Import 'from P02_SignIn' successful")
except ModuleNotFoundError as e:
    print(f"Import 'from P02_SignIn' failed: {e}")

try:
    from Pages.P02_SignIn import SignIn
    print("Import 'from Pages.P02_SignIn' successful")
except ModuleNotFoundError as e:
    print(f"Import 'from Pages.P02_SignIn' failed: {e}")
