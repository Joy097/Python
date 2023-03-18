import paramiko
import time

hostname = '192.168.114.132'
username = 'desktop-lndeaqh\jabir'
password = 'jabir123'

ssh = paramiko.SSHClient()
ssh.set_missing_host_key_policy(paramiko.AutoAddPolicy())
ssh.connect(hostname=hostname, username=username, password=password)

# Transfer file using sftp
sftp = ssh.open_sftp()
sftp.put(localpath='C:\\Users\\shiha\\OneDrive\\Desktop\\Python-main\\windows_automate\\uptime.py', remotepath='C:\\Users\\shiha\\Desktop\\scripts\\uptime.py')
sftp.close()

stdin, stdout, stderr = ssh.exec_command('python C:\\Users\\shiha\\Desktop\\uptime.py')
print(stdout.read().decode())
ssh.close()

