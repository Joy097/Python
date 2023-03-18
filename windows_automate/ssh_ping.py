import wmi
ip = '192.168.114.132'
username = 'desktop-lndeaqh\jabir'
password = 'jabir123'
conn = wmi.WMI(ip, user=username, password=password)
ping_status = conn.Win32_PingAddress(Address=ip)[0].StatusCode
if ping_status == 0:
    print("Connection successful!")
else:
    print("Connection failed.")
