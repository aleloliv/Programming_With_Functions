from address import extract_city, extract_state, extract_zipcode 
import pytest

address = "525 S Center St, Rexburg, ID 83460"

def test_extract_city():
    city = extract_city(address)
    assert city == "Rexburg"
    
def test_extract_state():
    state = extract_state(address)
    assert state == "ID"
    
def test_extract_zipcode():
    zipcode = extract_zipcode(address)
    assert zipcode == "83460"


# Call the main function that is part of pytest so that the
# computer will execute the test functions in this file.
pytest.main(["-v", "--tb=line", "-rN", __file__])

