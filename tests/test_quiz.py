from app.quiz import calculate_score


def test_score():
    answers = [True, False, True]
    assert calculate_score(answers) == 2


