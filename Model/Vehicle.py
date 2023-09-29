class Vehicle():
    def __init__(
            self: object, 
            name: str, 
            color: str,
            width: float,
            height: float,
            length: float = 0.,
            speed: float = 0.,
            image_path: str = None,
        ):
        self.name = name
        self.color = color
        self.speed = speed
        self.theta = 0. # radians from the y-axis
        self.phi = 0. # radians from the z-axis
        self.x = 0.
        self.y = 0.
        self.z = 0.
        self.width = width
        self.height = height
        self.length = length
        self.image_path = image_path

    def move(self, x: float, y: float, z: float):
        raise NotImplementedError("move() not implemented")

    def turn(self, theta: float, phi: float):
        raise NotImplementedError("turn() not implemented")
    
    def drive(self, x: list[float], y: list[float], theta: list[float], **kwargs):
        raise NotImplementedError("drive() not implemented")

    def __str__(self):
        return self.name + " " + self.color + " " + str(self.speed)
    