# By
# ████████╗██╗   ██╗ █████╗ ███╗   ██╗    ██╗  ██╗ ██████╗ 
# ╚══██╔══╝██║   ██║██╔══██╗████╗  ██║    ██║  ██║██╔═══██╗
#    ██║   ██║   ██║███████║██╔██╗ ██║    ███████║██║   ██║
#    ██║   ██║   ██║██╔══██║██║╚██╗██║    ██╔══██║██║   ██║
#    ██║   ╚██████╔╝██║  ██║██║ ╚████║    ██║  ██║╚██████╔╝
#    ╚═╝    ╚═════╝ ╚═╝  ╚═╝╚═╝  ╚═══╝    ╚═╝  ╚═╝ ╚═════╝ 

# Email: ttuan.ho@outlook.com                                                         

import os, sys
import time
from datetime import datetime
import subprocess
from config.config import check_log_file_str, sending_py_file_str, submit_log_str, git_log_str, sending_ans_files_str

def sh(cmd):
    subprocess.call(cmd, shell=True)

"""
Configuring data
"""
#  zid
zid = "z5261243"
className = "cs2511"

# folder to store on the cse machine
examFolder = "exam-demo"

# git repo for back up
remote_repo_url = "https://github.com/ttuanho/exam-wrapper.git"

questions = {
    "part2Q1A": False,
    "part2Q1B": False,
    "part2Q1C": False,
    "part2Q2A": False,
    "part2Q2B": False,
    "part2Q2C": False,
    "part2Q3": True,
    "part3Q1": True,
    "part3Q2": True,
    "part3Q3" : True
}

# the seconds to resubmit periodically
submitInterval = 8

# the end time to submit
# Attributes: year, month, day, hour, minute, second, microsecond
deadline = datetime(2020,8,16,21,49,59).timestamp()
lastSubmitTime = None
lastSendTime = None

def createFiles():
    for d, f in questions.items():
        if (os.path.exists(f"./answers/{d}") == False):
            sh(f"mkdir ./answers/{d}")
        if (f == False):
            sh(f"touch answers/{d}/{d}.txt")
    
    sh(f"touch {git_log_str}")
    sh(f"touch {submit_log_str}")
    sh(f"touch {check_log_file_str}")
    sh(f"touch {sending_ans_files_str}")
    sh(f"touch {sending_py_file_str}")

    sh(f"scp -r config/ {zid}@cse.unsw.edu.au:~/{examFolder}")

def backup2CSE():
    """
    Back up relevant files in the current dir to cse root/examFolder
    """
    sh(f"scp -r answers/ {zid}@cse.unsw.edu.au:~/{examFolder}")
    sh(f"scp -r *.py {zid}@cse.unsw.edu.au:~/{examFolder}")

def backupGit(msg):
    """
    Git wrapper
    """
    if (os.path.exists(".git") == False):
        sh("git init")
        sh("git add .")
        sh("git commit -m \"intial commit\"")
        sh(f"git remote add origin {remote_repo_url}")
        sh("git push -f -u origin master")
    else:
        sh("git add .") 
        now_str = datetime.now().strftime("%d/%m/%Y %H:%M:%S")
        sh(f"git commit -m \"Bot@{now_str}:{msg}\"") 


def pull_logs_back2Local():
    sh(f"scp -r {zid}@cse.unsw.edu.au:~/{examFolder}/logs .")
    
# This func is not needed if running another process on cse
def submit_subshell():
    sh(f"ssh -Y {zid}@cse.unsw.edu.au 'cd {examFolder}' && python3 auto_submit.py && logout")

def timer():
    while (True):
        global lastSendTime
        now = time.time()
        if (now < deadline and\
            ((lastSendTime == None) or\
            (now - lastSendTime > submitInterval))):
            backup2CSE()
            backupGit(" committed changes")
            submit_subshell()
            pull_logs_back2Local()
            lastSendTime = time.time()
        if (time.time() > deadline):
            pull_logs_back2Local()
            print(f">> Time out: the script now breaks")            
            break
    

if __name__ == "__main__":
    createFiles()
    timer()
