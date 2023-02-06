import os 
import subprocess
import shlex
import time
import traceback

list_scripts = ['instagram.py', 'readscreen.py'] #'senddatatoserverinsta.py', 'appleid.py', 'senddatatoserverapple.py', 'applecode.py'
start_time = time.time()
for script in list_scripts: 
	
     shell_cmd = ("python3 %s" % script) 
     subprocess_cmd = shlex.split(shell_cmd) 
     subprocess.call(subprocess_cmd)
print("--- %s seconds ---" % (time.time() - start_time))

