from app.quiz import calculate_score, start_quiz


def test_score():
    answers = [True, False, True]
    assert calculate_score(answers) == 2


def test_start_quiz(monkeypatch, capsys):
    user_inputs = [
        "git init",
        "git push",
        "git add",
        "git commit",
        "git pull",
    ]

    monkeypatch.setattr("builtins.input", lambda prompt="": user_inputs.pop(0))

    start_quiz()

    captured = capsys.readouterr()
    assert "Correct" in captured.out
    assert "Final Score: 5/5" in captured.out


