import paramiko

hostname = 'ip'
username = 'usrname'
password = 'pass'

# Connect to the remote device
ssh = paramiko.SSHClient()
ssh.set_missing_host_key_policy(paramiko.AutoAddPolicy())
ssh.connect(hostname=hostname, username=username, password=password)

# Run a file in certain location
stdin, stdout, stderr = ssh.exec_command('python C:\\Users\\shiha\\Desktop\\uptime.py')
print(stdout.read().decode())
ssh.close()

