import paramiko

def connect():
    hostname = input("Put the Hostname: ")
    username = input("Put the Username: ")
    password = input("Put the Password: ")
    ssh = paramiko.SSHClient()
    ssh.set_missing_host_key_policy(paramiko.AutoAddPolicy())
    ssh.connect(hostname=hostname, username=username, password=password)
    sftp = ssh.open_sftp()
    return sftp

def getFile():
    sftp = connect()
    sftp.get(remotepath='C:\\Users\\bosadmin\\Desktop\\uptime.py', localpath='C:\\Users\\sh.chowdhury\\Desktop\\airbnb_js\\up.py')

def putFile():
    sftp = connect()
    sftp.put(localpath='C:\\Users\\sh.chowdhury\\Desktop\\airbnb_js\\up.py', remotepath='C:\\Users\\bosadmin\\Desktop\\uptime.py')



print("enter the credentials for the server you want to get the file")
getFile()
print("enter the credentials for the server you want to put the file")
putFile()


