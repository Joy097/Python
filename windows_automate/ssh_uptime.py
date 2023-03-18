import wmi

# Set the credentials for the remote login
username = "desktop-lndeaqh\jabir"
password = "jabir123"

# Connect to the remote machine
remote_pc = "DESKTOP-LNDEAQH"
conn = wmi.WMI(remote_pc, user=username, password=password)

# Launch a new process that runs as the specified user
cmd = "C:\\Windows\\System32\\cmd.exe"
startup = conn.Win32_ProcessStartup.new()
startup.ShowWindow = 1  # Show the command prompt window
pid, result = conn.Win32_Process.Create(CommandLine=cmd, ProcessStartupInformation=startup)
if result == 0:
    print(f"Successfully launched process with PID {pid}")
else:
    print(f"Failed to launch process with error code {result}")
