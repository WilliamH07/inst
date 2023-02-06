import hashlib
import time
import os 
import subprocess
import shlex

import traceback

base=("d41d8cd98f00b204e9800998ecf8427e")

while(True):
    time.sleep(10)
    if(hashlib.md5(f.read()).hexdigest() != base):

            list_scripts = ['launch.py'] 
            start_time = time.time()
            for script in list_scripts: 
	
                shell_cmd = ("python3 %s" % script) 
                subprocess_cmd = shlex.split(shell_cmd) 
                subprocess.call(subprocess_cmd)
                print("--- %s seconds ---" % (time.time() - start_time))
    else: 
            print("not change")
        
