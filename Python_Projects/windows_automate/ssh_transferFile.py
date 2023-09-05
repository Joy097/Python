import paramiko

hostname = 'ip'
username = 'usrname'
password = 'pass'

# Connect to the remote device
ssh = paramiko.SSHClient()
ssh.set_missing_host_key_policy(paramiko.AutoAddPolicy())
ssh.connect(hostname=hostname, username=username, password=password)

# Transfer file using sftp
sftp = ssh.open_sftp()
sftp.put(localpath='C:\\Users\\shiha\\OneDrive\\Desktop\\Python-main\\windows_automate\\uptime.py', remotepath='C:\\Users\\shiha\\Desktop\\uptime.py')
sftp.close()