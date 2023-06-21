import glob
import os
import sys 
sys.path.insert(0, os.getcwd())
from src.utils import AppPath
from base import Captured_data_raw



# print(glob.glob("./data/captured_data/phase-1/prob-1/*"))

print(os.listdir("./data/captured_data/phase-1/prob-1"))



