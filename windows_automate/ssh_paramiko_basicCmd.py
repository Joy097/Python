import paramiko

# Set the hostname, username, and password for the remote PC
hostname = 'ip'
username = 'usrname'
password = 'pass'



ssh = paramiko.SSHClient()

# Automatically add the remote PC's host key
ssh.set_missing_host_key_policy(paramiko.AutoAddPolicy())

# Connect to the remote PC using the SSH protocol
ssh.connect(hostname, username=username, password=password)

# Run a command on the remote PC
stdin, stdout, stderr = ssh.exec_command('ipconfig')

# Print the output of the command
print(stdout.read().decode())

# Close the SSH connection
ssh.close()
