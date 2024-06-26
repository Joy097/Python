import subprocess
import time    #changeable
import os
import datetime


repo_dir = input("Enter the path to the local git repository: ").strip()
time_intv = float(input("Enter the time(min) interval to push: ").strip()) #changeable
file = input("Enter the file name or press '.' for multiple files: ").strip()

os.chdir(repo_dir)


ask = input("Is this your first push for this folder? (y/n): ").strip().lower()
if ask =='y':
    
    cmd = ["git", "init"]
    subprocess.call(cmd)
    

    sshKey = input("Enter your ssh key: ").strip()
    cmd = ["git", "remote", "add", "origin", sshKey]
    subprocess.call(cmd)
    
    
    
branch = input("new branch?(y/n): ")


if branch == "n":
    branch_name = input("Enter the old branch name: ").strip()
    if branch_name != "master":
        cmd = ["git", "checkout", branch_name]
        subprocess.call(cmd)
else:
    branch_name = input("Enter the current branch name: ").strip()
    cmd = ["git", "checkout", "-b", branch_name]
    subprocess.call(cmd)


    


    
      

print("Pushing files...")

count = 0

while True:
    cmd = ["git", "add", file]
    subprocess.call(cmd)


    #commit_message = input("Give a commit message: ") #changeable
    cmd = ["git", "commit", "-m", "update %s"%count]
    subprocess.call(cmd)


    cmd = ["git", "push", "origin", branch_name]
    subprocess.call(cmd)
    count+=1
    print(f"Pushed at: {datetime.datetime.now()}")
    
    time.sleep(time_intv*60)   #changeable
