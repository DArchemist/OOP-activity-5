from PyQt5.QtWidgets import QApplication
import sys
from ui.grades import UI

app = QApplication(sys.argv)
UIWindow = UI()
app.exec_()