#!/usr/bin/env python3
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.common.keys import Keys
import os
import sys
import inspect

#! usable to grab other created imports easier
currentdir = os.path.dirname(os.path.abspath(inspect.getfile(inspect.currentframe())))
# extract the path to parent directory
parentdir = os.path.dirname(currentdir)
# insert path to the folder from parent directory from which the python module/ file is to be imported
sys.path.insert(0, parentdir)
# insert path to folder from parent directory.
sys.path.insert(0, parentdir+'\\resources')
sys.path.insert(0, parentdir+'\\utility')

# from resources import Locators
# from utility import utility 





