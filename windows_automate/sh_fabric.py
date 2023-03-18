from fabric import Connection

# Define the connection parameters

hostname = '192.168.114.132'
username = 'desktop-lndeaqh\jabir'
password = 'jabir123'

# Create the connection object
c = Connection(host=hostname, user=username, connect_kwargs={"password": password})

# Run a command on the remote server
result = c.run('ls -al')
print(result.stdout)
