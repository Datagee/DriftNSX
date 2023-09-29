from Model.Car import Car

did_call_callback = False
def test_drive():
    car = Car("test_car", speed=2)
    def callback():
        global did_call_callback
        did_call_callback = True

    try:
        car.drive([1, 1], [1, 1], [1, 1, 1], callback)
        assert False
    except ValueError:
        pass

    car.drive([1, 1], [1, 1], [1, 1], callback)

    assert car.x == 2
    assert car.y == 2
    assert car.theta == 1
    assert did_call_callback

