"""
  Author : Balaji Nagaiahgari
  This python program prints the contents of a given directory from the local machine.

  pre-requisite : import os module ----> pip install os
"""

import os

directory_path="/Balaji/Marriage"

contents=os.listdir(directory_path)

for item in contents:
    print(item)

