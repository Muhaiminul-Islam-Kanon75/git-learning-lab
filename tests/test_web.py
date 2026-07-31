from app.web import evaluate_quiz, get_questions_payload, simulate_command_payload


def test_get_questions_payload():
    payload = get_questions_payload()

    assert payload["questions"][0]["question"].startswith("Which command")
    assert len(payload["questions"]) == 5


def test_evaluate_quiz():
    payload = evaluate_quiz(
        ["git init", "git push", "git add", "git commit", "git pull"]
    )

    assert payload["score"] == 5
    assert payload["results"][0]["correct"] is True


def test_simulate_command_payload():
    payload = simulate_command_payload("init")

    assert payload["result"] == "git init"
