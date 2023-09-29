from Model.AcuraNSX import AcuraNSX
from Model.Car import Transmission

def test_nsx_width():
    car = AcuraNSX()
    assert 156 <= car.width <= 300

def test_nsx_color():
    car = AcuraNSX()
    assert car.color == "red"

def test_nsx_transmission():
    car = AcuraNSX()
    assert car.transmission == Transmission.MANUAL

def test_nsx_name():
    car = AcuraNSX()
    assert car.name == "Acura NSX"

def test_nsx_speed():
    car = AcuraNSX()
    assert car.speed == 5