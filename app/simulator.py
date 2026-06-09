SUPPORTED_COMMANDS = {
    "git init": "Initialized empty Git repository",
    "git status": "Shows current repository status",
    "git add": "Adds files to staging area",
    "git commit": "Creates a snapshot commit",
    "git push": "Uploads commits to remote repository",
}



def simulate_command(command: str):
    response = SUPPORTED_COMMANDS.get(command)

    if response:
        print(response)
    else:
        print("Unsupported command")
