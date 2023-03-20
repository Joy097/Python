# Establish ssh
We need to install OpenSSH to use a machine as a remote host. To do so, 
- We need to goto Optional features section in the apps and features section. Then add feature > select open ssh > Done
- Set a rule by going to Windows Defender Firewall with Advanced Security > Inbound Rules > new rules > port > select TCP and Specify 22 > Allow all connection > check and finish
- Finally, ctrl+r > services.msc > right click OpenSSH and start

Now you can access the remote device with port 22 for ssh operations.

## Windows Server 2016 Setup
- There is no OpenSSH server installed in this version. So, have to install it externally using powershell. Commands are:
    - 