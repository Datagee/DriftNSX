from Model.Vehicle import Vehicle
from enum import IntEnum

class Transmission(IntEnum):
    AUTOMATIC = 1
    MANUAL = 2

class Car(Vehicle):
    def __init__(
            self, 
            name, 
            color: str = "black", 
            speed: float = 1., 
            width: float = 100.,
            height: float = 100.,
            num_doors: int = 4, 
            transmission: Transmission = Transmission.AUTOMATIC,
            *args,
            **kwargs,
        ):
        super().__init__(
            name, 
            color, 
            width,
            height,
            0.,
            speed,
            *args,
            **kwargs,
        )
        self.num_doors = num_doors
        self.transmission = transmission

    def __str__(self):
        return super().__str__() + " " + str(self.num_doors) + " " + str(self.transmission)

    def turn(self, theta: float, _):
        self.theta = theta
    
    def move(self, x: float, y: float, _):
        """
            Moves the car by x and y

            :param x: the amount to move the car in the x direction
            :type x: float
            :param y: the amount to move the car in the y direction
            :type y: float
        """
        self.x = x
        self.y = y

