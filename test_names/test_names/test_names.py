from names import make_full_name, \
    extract_family_name, extract_given_name
import pytest

def test_make_full_name():
    full_name = make_full_name("Alexandre", "Oliveira")
    assert full_name == "Oliveira; Alexandre"
    
    full_name = make_full_name("Ann", "Man")
    assert full_name == "Man; Ann"
    
    full_name = make_full_name("Mary", "Holland-White")
    assert full_name == "Holland-White; Mary"
    
def test_extract_family_name():
    family_name = extract_family_name("Oliveira; Alexandre")
    assert family_name == "Oliveira"
    
    family_name = extract_family_name("Man; Ann")
    assert family_name == "Man"

    family_name = extract_family_name("Holland-White; Mary")
    assert family_name == "Holland-White"

    
def test_extract_given_name():
    given_name = extract_given_name("Oliveira; Alexandre")
    assert given_name == "Alexandre"
    
    given_name = extract_given_name("Man; Ann")
    assert given_name == "Ann"

    given_name = extract_given_name("Holland-White; Mary")
    assert given_name == "Mary"

# Call the main function that is part of pytest so that the
# computer will execute the test functions in this file.
pytest.main(["-v", "--tb=line", "-rN", __file__])
