#ADB ANDROID 

import subprocess
import shlex
import time
#APPLE
shell_cmd = ("adb shell input tap %s" % "487 130")
subprocess_cmd = shlex.split(shell_cmd)
subprocess.call(subprocess_cmd)

shell_cmd = ("adb shell input keyevent %s" % "66")
subprocess_cmd = shlex.split(shell_cmd)
subprocess.call(subprocess_cmd)
time.sleep(2)
shell_cmd = ("adb shell input tap %s" % "533 1669")
subprocess_cmd = shlex.split(shell_cmd)
subprocess.call(subprocess_cmd)
time.sleep(1)
with open("credentials.txt", mode="r", encoding="utf-8") as file:
    for line in file:

        ipv6 = (f"{line.rstrip()}")
        shell_cmd = ("adb shell input text %s" % ipv6)
        subprocess_cmd = shlex.split(shell_cmd)
        subprocess.call(subprocess_cmd)
        
        shell_cmd = ("adb shell input keyevent %s" % "66")
        subprocess_cmd = shlex.split(shell_cmd)
        subprocess.call(subprocess_cmd)
        
        ipv6 = (f"{line.rstrip()}")
        shell_cmd = ("adb shell input text %s" % ipv6)
        subprocess_cmd = shlex.split(shell_cmd)
        subprocess.call(subprocess_cmd)

        shell_cmd = ("adb shell input keyevent %s" % "66")
        subprocess_cmd = shlex.split(shell_cmd)
        subprocess.call(subprocess_cmd)

shell_cmd = ("adb shell input tap %s" % "535 1415")
subprocess_cmd = shlex.split(shell_cmd)
subprocess.call(subprocess_cmd)