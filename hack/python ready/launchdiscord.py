import subprocess
import time

while True:
    subprocess.run(["python", "getdata.py"])
    subprocess.run(["python", "senddatatodiscord.py"])
    time.sleep(300)
