#!/usr/bin/env python3

import subprocess
import os
import sys
from concurrent import futures


path=sys.argv[1]

list = os.listdir()

def copy(i,path):
	subprocess.run(['cp','-rv',i,path])


executor = futures.ThreadPoolExecutor()   #In place of Thread we can use 'Process'
for i in list:
	executor.submit(copy,i,path)  #executor will run all the task in parallel

print("waiting for all files to copy")  #loop will be finished as soon as all the task are scheduled hence writing this message
executor.shutdown()
