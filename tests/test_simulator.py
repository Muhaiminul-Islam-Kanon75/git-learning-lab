from app.simulator import get_git_command


def test_git_command():
    assert get_git_command("clone").startswith("git")