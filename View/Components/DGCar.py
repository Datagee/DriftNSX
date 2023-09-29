from tkinter import Canvas, Widget, Label
from PIL import Image, ImageTk
from Model.Car import Car
import math
import numpy as np

class DGCar(Canvas):
    def __init__(
            self: Canvas, 
            master: Widget, 
            car: Car,
            width: int = 500,
            height: int = 500,
        ):
        
        super().__init__(
            master,
            width=width,
            height=height,
        )
        self.width = width
        self.height = height
        self.root = master
        self.car = car
        self.car_image = Image.open(self.car.image_path)
        self.rendered_car: ImageTk.PhotoImage = ImageTk.PhotoImage(self.car_image)
        self.car_label = Label(
            self,
            width=int(self.car.width),
            height=int(self.car.height),
            image=self.rendered_car,
        )
        self.draw()
    
    def draw(self):
        """
            Draws the car on the canvas
        """
        if self.winfo_ismapped():
            self.place_forget()

        self.car_label.config(
            width=self.car.width,
            height=self.car.height,
        )

        self.car_label.place(
            x=self.car.x,
            y=self.car.y,
        )
        self.update_car_image()
        self.root.update()
       
    def radians_to_degrees(self, radians: float):
        """
            Converts radians to degrees

            :param radians: The angle in radians
            :type radians: float
            :return: The angle in degrees
            :rtype: float
        """
        return radians * 180 / math.pi

    def update_car_image(self):
        """
            Updates the car image based on the current
            value of self.theta
        """
        rotated = self.car_image.rotate(-self.radians_to_degrees(self.car.theta), resample=Image.BICUBIC)
        self.rendered_car = ImageTk.PhotoImage(rotated)
        self.car_label.configure(image=self.rendered_car)
    def drift(self):
        radians = np.linspace(0,math.pi/2,400)
        degrees = [i for i in range(0,400)]
        for r in radians:
            degrees.append(self.radians_to_degrees(r))
        x = []
        y = []
        for i in range(len(radians)):
            x.append(i/30*math.cos(radians[i]))
            y.append(i/30*math.sin(radians[i]))
        self.car.drive(x,y,radians,self.draw) 