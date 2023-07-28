from subprocess import run
from datetime import datetime

class COLORS:
    okgreen = "\033[92m"
    okcyan = '\033[96m'
    warning = "\033[93m"
    fail = "\033[91m"
    endc = "\033[0m"

class GitManager:

    def push():
        try:
            run("git add world_data/", shell=True)
            run(f'git commit -m "World save: {datetime.now()}"', shell=True)
            run("git push", shell=True)
        except Exception as e:
            print(f"Error occured when pushing.\n{e}")

    def pull():
        try:
            run("git pull", shell=True)
        except Exception as e:
            print(f"Error occured when pulling.\n{e}")
    