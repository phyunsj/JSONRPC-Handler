#!/usr/bin/env python
from string import Template
import sys, pprint, os
import re
import json
import time
import shutil

# Add the directory containing your module to the Python path
scriptpath = "./scannerTypes.py"
sys.path.append(os.path.abspath(scriptpath))
from scannerTypes import *

scriptpath = "./scannerMethods.py"
sys.path.append(os.path.abspath(scriptpath))
from scannerMethods import *

if __name__ == '__main__':

    types = scannerTypes()
    types.codegen( [ 'user_defined_types'] )

    methods = scannerMethods()
    methods.codegen( [ 'math'] )