from Model.Vehicle import Vehicle
from Model.Car import Car
from enum import IntEnum
from Model.Car import Transmission

class AcuraNSX(Car):
    def __init__(
            self, 
            name: str = "Acura NSX", 
            color: str = "red", 
            speed: float = 5, 
            width: float = 156., 
            height: float = 200.,
            num_doors: int = 2, 
            transmission: Transmission = Transmission.MANUAL,
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
        self.image_path = "assets/NSX.png"
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

