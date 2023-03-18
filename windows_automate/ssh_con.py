import win32com.client

remote_computer = "192.168.1.100"  # Replace with the IP address or name of the remote computer
username = "desktop-lndeaqh\jabir"  # Replace with the username of an account on the remote computer
password = "jabir123"  # Replace with the password for the account on the remote computer

locator = win32com.client.Dispatch("WbemScripting.SWbemLocator")
service = locator.ConnectServer(remote_computer, "root\\CIMV2", username, password)

# Now you can use the `service` object to execute WMI queries on the remote computer
