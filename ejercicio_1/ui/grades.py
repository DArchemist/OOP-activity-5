from PyQt5.QtWidgets import QDialog, QLabel, QLineEdit, QTextEdit, QPushButton
from PyQt5 import uic
import os
from modules.grades import Grades

class UI(QDialog):
    def __init__(self):
        super(UI, self).__init__()
        uic.loadUi(os.path.join("ui", "grades.ui"), self)

        # Defining widgets

        self.grade_1 = self.findChild(QLineEdit, "grade_1")
        self.grade_2 = self.findChild(QLineEdit, "grade_2")
        self.grade_3 = self.findChild(QLineEdit, "grade_3")
        self.grade_4 = self.findChild(QLineEdit, "grade_4")
        self.grade_5 = self.findChild(QLineEdit, "grade_5")

        self.grades_average = self.findChild(QLineEdit, "grades_average")
        self.grades_std_dev = self.findChild(QLineEdit, "grades_std_dev")
        self.highest_grade = self.findChild(QLineEdit, "highest_grade")
        self.lowest_grade = self.findChild(QLineEdit, "lowest_grade")

        self.compute_button = self.findChild(QPushButton, "compute_button")
        self.clear_button = self.findChild(QPushButton, "clear_button")

        self.show()

        self.compute_button.clicked.connect(self.compute_results)
        self.clear_button.clicked.connect(self.clear_all)

    
    def compute_results(self):
        grades_input = [self.grade_1, self.grade_2, self.grade_3, self.grade_4, self.grade_5]
        grades_list = [float(grade.text()) for grade in grades_input]
        grades = Grades(grades_list)

        self.grades_average.setText(str(grades.get_grades_average()))
        self.grades_std_dev.setText(str(grades.get_grades_std_dev()))
        self.highest_grade.setText(str(grades.get_highest_grade()))
        self.lowest_grade.setText(str(grades.get_lowest_grade()))

    def clear_all(self):
        elements = [
        self.grade_1,
        self.grade_2,
        self.grade_3,
        self.grade_4,
        self.grade_5,
        self.grades_average,
        self.grades_std_dev,
        self.highest_grade,
        self.lowest_grade]

        for element in elements:
            element.setText('')
