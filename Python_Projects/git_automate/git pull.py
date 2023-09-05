import subprocess
import os
import datetime

def del_all():
    files = os.listdir(repo_dir)

    for file in files:
        file_path = os.path.join(repo_dir, file)
        if os.path.isfile(file_path):
            os.remove(file_path)
            print(f"Deleted {file_path}")

def pull():
    sshKey = input("Enter your ssh key: ").strip()
    cmd = ["git", "clone",  sshKey]
    subprocess.call(cmd)

repo_dir = input("Enter the path to the local git repository: ").strip()
ask = input("Do you want to delete all files in the repository? (yes/n): ").strip()

os.chdir(repo_dir)

if ask == "yes":
    del_all()
    
pull()

