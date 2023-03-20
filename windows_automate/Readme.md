# Establish ssh
We need to install OpenSSH to use a machine as a remote host. To do so, 
- We need to goto Optional features section in the apps and features section. Then add feature > select open ssh > Done
- Set a rule by going to Windows Defender Firewall with Advanced Security > Inbound Rules > new rules > port > select TCP and Specify 22 > Allow all connection > check and finish
- Finally, ctrl+r > services.msc > right click OpenSSH and start

Now you can access the remote device with port 22 for ssh operations.

---

## Windows Server 2016 Setup
There is no OpenSSH server installed in this version. So, have to install it externally using powershell. Steps are:
- download the OpenSSH file
- powershell run as admin
- change directory to that specific OpenSSH folder
- Commands:
    - powershell.exe -ExecutionPolicy Bypass -File install-sshd.ps1
    - NewNetFirewallRule -Name sshd -DisplayName "OpenSSH Server" -Enabled True -Direction Inbound -Protocol TCP -Action Allow -LocalPort 22
    - goto Run > services.msc 
    - Start both OpenSSH server and OpenSSH Authentication

---

## Secured Network
- maybe there is python but both python and pip location path have to be in the environment variable
- pip may not work in this network. So, use different network to use it
- in secured network windows server, package file is not present. So, at first pip install in your machine and then copy paste to the remote server using the 