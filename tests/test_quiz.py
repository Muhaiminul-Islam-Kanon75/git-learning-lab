from app.quiz import QUESTIONS


def test_questions_exist():
    assert len(QUESTIONS) > 0