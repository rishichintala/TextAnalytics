import os
import sys
# Python defines two types of packages, regular packages and namespace packages. 
# Regular packages are traditional packages as they existed in Python 3.2 and earlier. 
# A regular package is typically implemented as a directory containing an __init__.py file. 
# When a regular package is imported, this __init__.py file is implicitly executed, 
# and the objects it defines are bound to names in the package’s namespace. 
# The __init__.py file can contain the same Python code that any other module can contain, 
# and Python will add some additional attributes to the module when it is imported.

# https://docs.python.org/3/reference/import.html#namespace-packages
print("current python path is:\n" + '\n'.join(sys.path))
print("__init__.py is used to better organize code and to run any initialization that should be run automatically when the package is imported")
