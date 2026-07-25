from PySide6.QtWidgets import QMainWindow, QWidget, QHBoxLayout

from gui.sidebar import Sidebar
from gui.dashboard import Dashboard


class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()

        self.setWindowTitle("PB7 Intelligence Studio")
        self.resize(1400, 900)

        container = QWidget()
        layout = QHBoxLayout()

        self.sidebar = Sidebar()
        self.dashboard = Dashboard()

        layout.addWidget(self.sidebar)
        layout.addWidget(self.dashboard)

        container.setLayout(layout)

        self.setCentralWidget(container)