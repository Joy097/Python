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

repo_dir = input("Enter the path to the local git repository: ").strip()
#os.chdir(repo_dir)

