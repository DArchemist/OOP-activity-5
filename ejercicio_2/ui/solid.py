from PyQt5.QtWidgets import QMainWindow, QDialog, QLabel, QLineEdit, QTextEdit, QPushButton
from PyQt5 import uic
import os
from modules.cylinder import Cylinder
from modules.sphere import Sphere
from modules.pyramid import Pyramid

class UI(QMainWindow):
    def __init__(self):
        super().__init__()
        uic.loadUi(os.path.join("ui", "main_window.ui"), self)

        self.show()

        self.cylinder_button = self.findChild(QPushButton, "cylinder_button")
        self.sphere_button = self.findChild(QPushButton, "sphere_button")
        self.pyramid_button = self.findChild(QPushButton, "pyramid_button")

        self.cylinder_button.clicked.connect(self.show_cylinder_dialog)
        self.sphere_button.clicked.connect(self.show_sphere_dialog)
        self.pyramid_button.clicked.connect(self.show_pyramid_dialog)

    def show_cylinder_dialog(self):
        dialog = CylinderDialog(self)
        dialog.exec_()

    def show_sphere_dialog(self):
        dialog = SphereDialog(self)
        dialog.exec_()

    def show_pyramid_dialog(self):
        dialog = PyramidDialog(self)
        dialog.exec_()


class CylinderDialog(QDialog):
    def __init__(self, parent=None):
        super().__init__(parent)
        uic.loadUi(os.path.join("ui", "cylinder.ui"), self)

        self.radius = self.findChild(QLineEdit, "radius")
        self.shape_height = self.findChild(QLineEdit, "height")

        self.compute_button = self.findChild(QPushButton, "compute_button")

        self.volume = self.findChild(QLineEdit, "volume")
        self.surface = self.findChild(QLineEdit, "surface")

        self.compute_button.clicked.connect(self.compute_results)

    def compute_results(self):
        cylinder = Cylinder(float(self.radius.text()), float(self.shape_height.text()))
        self.volume.setText(str(cylinder.get_volume()))
        self.surface.setText(str(cylinder.get_surface()))


class SphereDialog(QDialog):
    def __init__(self, parent=None):
        super().__init__(parent)
        uic.loadUi(os.path.join("ui", "sphere.ui"), self)

        self.radius = self.findChild(QLineEdit, "radius")

        self.compute_button = self.findChild(QPushButton, "compute_button")

        self.volume = self.findChild(QLineEdit, "volume")
        self.surface = self.findChild(QLineEdit, "surface")

        self.compute_button.clicked.connect(self.compute_results)

    def compute_results(self):
        sphere = Sphere(float(self.radius.text()))
        self.volume.setText(str(sphere.get_volume()))
        self.surface.setText(str(sphere.get_surface()))


class PyramidDialog(QDialog):
    def __init__(self, parent=None):
        super().__init__(parent)
        uic.loadUi(os.path.join("ui", "pyramid.ui"), self)

        self.base = self.findChild(QLineEdit, "base")
        self.shape_height = self.findChild(QLineEdit, "height")
        self.apothem = self.findChild(QLineEdit, "apothem")

        self.compute_button = self.findChild(QPushButton, "compute_button")

        self.volume = self.findChild(QLineEdit, "volume")
        self.surface = self.findChild(QLineEdit, "surface")

        self.compute_button.clicked.connect(self.compute_results)

    def compute_results(self):
        pyramid = Pyramid(float(self.base.text()), float(self.shape_height.text()), float(self.apothem.text()))
        self.volume.setText(str(pyramid.get_volume()))
        self.surface.setText(str(pyramid.get_surface()))