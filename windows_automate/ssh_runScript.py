import paramiko

ssh = paramiko.SSHClient()
ssh.set_missing_host_key_policy(paramiko.AutoAddPolicy())
ssh.connect(hostname='remote-host', username='username', password='password')

sftp = ssh.open_sftp()

