import os
import re
import sys

change_dir = re.search(r'(.+AutomationMaster).+', os.getcwd()).group(1)
sys.path.insert(0, change_dir)
