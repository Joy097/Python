from paramiko import SSHClient, AutoAddPolicy
from rich import print, pretty, inspect
pretty.install()

client = SSHClient()
#LOAD HOST KEYS
#client.load_host_keys('~/.ssh/known_hosts')
client.load_host_keys('C:/Users/shiha/.ssh/known_hosts')
client.load_system_host_keys()

#Known_host policy
client.set_missing_host_key_policy(AutoAddPolicy())


#client.connect('10.1.1.92', username='root', password='password1')
client.connect('192.168.114.132', username='desktop-lndeaqh\jabir', password='jabir123')


# Run a command (execute PHP interpreter)
#client.exec_command('hostname')
stdin, stdout, stderr = client.exec_command('hostname')
print(type(stdin))
print(type(stdout))
print(type(stderr))

# Optionally, send data via STDIN, and shutdown when done
stdin.write('Hello world')
stdin.channel.shutdown_write()

# Print output of command. Will wait for command to finish.
print(f'STDOUT: {stdout.read().decode("utf8")}')
print(f'STDERR: {stderr.read().decode("utf8")}')

# Get return code from command (0 is default for success)
print(f'Return code: {stdout.channel.recv_exit_status()}')

# Because they are file objects, they need to be closed
stdin.close()
stdout.close()
stderr.close()

# Close the client itself
client.close()