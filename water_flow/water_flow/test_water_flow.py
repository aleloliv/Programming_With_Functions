from pytest import approx
import pytest
from water_flow import water_column_height, pressure_gain_from_water_height, pressure_loss_from_pipe, pressure_loss_from_fittings, reynolds_number, pressure_loss_from_pipe_reduction, psi_from_kpa

def test_water_column_height():
    water_c_height = water_column_height(0, 0)
    assert water_c_height == 0

    water_c_height = water_column_height(0, 10)
    assert water_c_height == 7.5
    
    water_c_height = water_column_height(25, 0)
    assert water_c_height == 25
    
    water_c_height = water_column_height(48.3, 12.8)
    assert water_c_height == 57.9
    
def test_pressure_gain_from_water_height():
    pressure = pressure_gain_from_water_height(0)
    assert pressure == approx(0, abs=0.001)
    
    pressure = pressure_gain_from_water_height(30.2)
    assert pressure == approx(295.628, abs=0.001)

    pressure = pressure_gain_from_water_height(50)
    assert pressure == approx(489.450, abs=0.001)
    
def test_pressure_loss_from_pipe():
    pressure = pressure_loss_from_pipe(0.048692, 0, 0.018, 1.75)
    assert pressure == approx(0, abs=0.001)
    
    pressure = pressure_loss_from_pipe(0.048692, 200, 0, 1.75)
    assert pressure == approx(0, abs=0.001)
    
    pressure = pressure_loss_from_pipe(0.048692, 200, 0.018, 0)
    assert pressure == approx(0, abs=0.001)
    
    pressure = pressure_loss_from_pipe(0.048692, 200, 0.018, 1.75)
    assert pressure == approx(-113.008, abs=0.001)
    
    pressure = pressure_loss_from_pipe(0.048692, 200, 0.018, 1.65)
    assert pressure == approx(-100.462, abs=0.001)
    
    pressure = pressure_loss_from_pipe(0.28687, 1000, 0.013, 1.65)
    assert pressure == approx(-61.576, abs=0.001)
    
    pressure = pressure_loss_from_pipe(0.28687, 1800.75, 0.013, 1.65)
    assert pressure == approx(-110.884, abs=0.001)

def test_pressure_loss_from_fittings():
    loss = pressure_loss_from_fittings(0, 3)
    assert loss == approx(0, abs=0.001)

    loss = pressure_loss_from_fittings(1.65, 0)
    assert loss == approx(0, abs=0.001)

    loss = pressure_loss_from_fittings(1.65, 2)
    assert loss == approx(-0.109, abs=0.001)

    loss = pressure_loss_from_fittings(1.75, 2)
    assert loss == approx(-0.122, abs=0.001)

    loss = pressure_loss_from_fittings(1.75, 5)
    assert loss == approx(-0.306, abs=0.001)

def test_reynolds_number():
    reynolds = reynolds_number(0.048692, 0)
    assert reynolds == approx(0, abs=1)

    reynolds = reynolds_number(0.048692, 1.65)
    assert reynolds == approx(80069, abs=1)

    reynolds = reynolds_number(0.048692, 1.75)
    assert reynolds == approx(84922, abs=1)

    reynolds = reynolds_number(0.28687, 1.65)
    assert reynolds == approx(471729, abs=1)

    reynolds = reynolds_number(0.28687, 1.75)
    assert reynolds == approx(500318, abs=1)

def test_pressure_loss_from_pipe_reduction():
    pressure_loss = pressure_loss_from_pipe_reduction(0.28687, 0, 1, 0.048692)
    assert pressure_loss == approx(0, 0.001)

    pressure_loss = pressure_loss_from_pipe_reduction(0.28687, 1.65, 471729, 0.048692)
    assert pressure_loss == approx(-163.744, 0.001)

    pressure_loss = pressure_loss_from_pipe_reduction(0.28687, 1.75, 500318, 0.048692)
    assert pressure_loss == approx(-184.182, 0.001)

def test_psi_from_kpa():
    psi = psi_from_kpa(1)
    assert psi == approx(0.145, abs=0.001)

    psi = psi_from_kpa(158.7)
    assert psi == approx(23.017, abs=0.001)

    psi = psi_from_kpa(179.3)
    assert psi == approx(26.005, abs=0.001)

# Call the main function that is part of pytest so that the
# computer will execute the test functions in this file.
pytest.main(["-v", "--tb=line", "-rN", __file__])