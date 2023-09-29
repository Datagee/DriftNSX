#!/usr/bin/env python3 
# -*- coding:utf-8 -*-

from View.Components.DGCar import DGCar
from Model.AcuraNSX import AcuraNSX
from tkinter import Tk

root = Tk()
root.geometry("1000x1000")
root.update()
car = DGCar(
    root, 
    AcuraNSX(), 
    width=root.winfo_width(), 
    height=root.winfo_height(),
)
car.pack()
car.drift()
