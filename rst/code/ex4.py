import subprocess
import sys

args = sys.argv
if len(args) == 1:
    print("command file name needed")
    sys.exit()

filename = args[1]

sshcmd = ["ssh", "picam"]
with open(filename) as fin:
    lines = fin.readlines()
    if len(lines) < 1:
        print("no commands found")
        sys.exit()
for l in lines:
    ls = l.strip()
    parts = ls.split()
    if len(parts) == 0: continue
    cmd = sshcmd + parts
    print("*"* 30)
    subprocess.run(parts)
