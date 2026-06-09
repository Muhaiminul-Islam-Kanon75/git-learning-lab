from app.simulator import SUPPORTED_COMMANDS

def test_git_init_exists():
    assert "git init" in SUPPORTED_COMMANDS

def test_git_push_exists():
    assert "git push" in SUPPORTED_COMMANDS