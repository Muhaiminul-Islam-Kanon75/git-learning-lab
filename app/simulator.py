SUPPORTED_COMMANDS = {
    "clone": "git clone <repo-url>",
    "init": "git init",
    "status": "git status",
    "add": "git add .",
    "commit": "git commit -m 'message'",
    "push": "git push origin main",
}


def get_git_command(command: str):
    return SUPPORTED_COMMANDS.get(command, "Unsupported command")


def simulate_command(command: str):
    result = get_git_command(command)

    if result != "Unsupported command":
        print(result)
    else:
        print("Unsupported command")