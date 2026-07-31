from app.simulator import get_git_command, simulate_command


def test_git_command():
    assert get_git_command("clone").startswith("git")


def test_simulate_command_supported(capsys):
    simulate_command("init")

    captured = capsys.readouterr()
    assert captured.out.strip() == "git init"


def test_simulate_command_unsupported(capsys):
    simulate_command("unknown")

    captured = capsys.readouterr()
    assert captured.out.strip() == "Unsupported command"
