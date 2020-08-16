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
from auto_send2CSE import sh, zid, examFolder, remote_repo_url, questions, submitInterval, deadline, lastSubmitTime, className
from config.config import check_log_file_str, sending_py_file_str, submit_log_str, git_log_str, sending_ans_files_str
from glob import glob

# submit all answer files
def give_all_answers():
    sh(f"rm {submit_log_str}")
    sh(f"touch {submit_log_str}")

    for d, f in questions.items():
        # submitting short answers
        if (f == False):
            if (os.path.exists(f"answers/{d}/{d}.txt") == False):
                continue
            sh(f"mv answers/{d}/{d}.txt .")
            sh(f"cat ./config/yes | give {className} {d} {d}.txt >> {submit_log_str} 2>&1")
            print(f"Submitted {d}")
            sh(f"rm {d}.txt")
            continue
        
        # submitting source code answers
        files_to_submit = []
        files_to_submit_str = " "
        for ff in glob('answers/'+d+'/**/*.java', recursive = True):
            # print(f"Found file {ff}")
            files_to_submit.append(ff)
            sh(f"cp {ff} .")
            files_to_submit_str += ff + " "
        
        if (files_to_submit == []):
            continue
        sh(f"cat ./config/yes | give {className} {d} *.java >> {submit_log_str} 2>&1")
        print(f"Submitted {d}")
        sh(f"rm *.java")


def update_check_log():
    """
    2511 classrun -check part2Q1A > logs/submission-check-log.txt 2>&1
    """
    sh(f"rm {check_log_file_str}")
    sh(f"touch {check_log_file_str}")
    for f in questions.keys():
        sh(f"2511 classrun -check {f} >> {check_log_file_str} 2>&1")

def timer():
    global lastSubmitTime
    now = time.time()
    while(True):
        if (now < deadline and\
            ((lastSubmitTime == None) or\
            (now - lastSubmitTime > submitInterval))):
            give_all_answers()
            update_check_log()
        if (time.time() > deadline):
            print(f">> Time out: the script now breaks")
            break


if __name__ == "__main__":
    give_all_answers()
    update_check_log()

    # Using seperate process 
    # timer()