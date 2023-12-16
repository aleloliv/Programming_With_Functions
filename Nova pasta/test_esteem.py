from esteem import questions, entry, score
import pytest

def test_question():
    question = questions(1)
    assert question == "2. I feel that I have a number of good qualities."

def test_entry():
    result = entry("A")
    assert result == "A"

def test_score():
    value = score(2, "a")
    assert value == 2

# Call the main function that is part of pytest so that the
# computer will execute the test functions in this file.
pytest.main(["-v", "--tb=line", "-rN", __file__])