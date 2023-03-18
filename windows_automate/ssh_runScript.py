import paramiko

hostname = '192.168.114.132'
username = 'desktop-lndeaqh\jabir'
password = 'jabir123'

ssh = paramiko.SSHClient()
ssh.set_missing_host_key_policy(paramiko.AutoAddPolicy())
ssh.connect(hostname, username, password)

# Transfer file using sftp
sftp = ssh.open_sftp()
sftp.put(local_path='C:/Users/shiha/OneDrive/Desktop/Python-main/windows_automate/uptime.py', remote_path='C:/Users/shiha/Desktop/uptime.py')
stdin, stdout, stderr = ssh.exec_command('python C:/Users/shiha/Desktop/uptime.py')
print(stdout.read().decode())
sftp.close()
ssh.close()

