import subprocess

output = subprocess.check_output("dir /p", shell=True)

print(output.decode('utf-8'))
