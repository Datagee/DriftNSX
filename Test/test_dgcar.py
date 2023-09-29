from View.Components.DGCar import DGCar
from Model.AcuraNSX import AcuraNSX
from tkinter import Tk, Toplevel

root = Toplevel() or Tk()

def test_drift():
    dg_car = DGCar(
        root, 
        AcuraNSX(), 
    )
    dg_car.drift()
    assert abs(dg_car.car.x - 1.22158e-13) < 0.00001
    assert abs(dg_car.car.y - 1995) < 0.00001