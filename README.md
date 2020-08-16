# Exam Wrapper

Since all exams have been moved to online and Vlab interface may seems not to be a good friend, this repo is created to publish the scripts that then will make the submssion of the answer files automatically and periodically to UNSW CSE servers.

In additions, the scripts also wrap around git to record the version over time.

## Introduction to CSE submission system / commands 



## License

Published under [MIT license](LICENSE).

# Guideline

- All the questions should be answered in the folder [./answers/](answers/)

## Other important notes

- Because the scripts adheres to the system or commands as described above, the repo is only applicable to UNSW CSE servers only.

- If running all the scripts as below, there're some logging to record all activities during the exam:
  - [logs/submit-log.txt](logs/submit-log.txt) records all the output from the `give` command
  - [logs/submission-check-log.txt](logs/submission-check-log.txt) records all the output from the `classrun -check` command


## Requirements

A few critical to make these submission scripts work:

- You must added RSA (public) key to CSE server. If you did, one way to test this is to login the server without typing password via `ssh -Y z555555@cse.unsw.edu.au`, where `z555555` should be replaced with your own zid.
- Python 3 (which is already installed on CSE server but may not be installed on your local machine yet)

## Critical things to do before the exam

1. Check if the all the configurations are correct. This include:
2. Locally, run `python3 auto_send2CSE.py`. This will periodically send your answer files to CSE servers.
3. On CSE server and in the exam folder, run `python3 auto_submit.py`. This will periodically make the submission for you.
4. Focus on the exam itself & nail it!

