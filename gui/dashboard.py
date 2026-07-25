from PySide6.QtWidgets import QWidget, QLabel, QVBoxLayout
from PySide6.QtCore import Qt


class Dashboard(QWidget):
    def __init__(self):
        super().__init__()

        layout = QVBoxLayout()

        label = QLabel(
            "PB7 Intelligence Studio\n\n"
            "Command Centre Online\n\n"
            "🟢 GUI Loaded\n"
            "🟢 Python Ready\n"
            "🟢 Workspace Active"
        )

        label.setAlignment(Qt.AlignCenter)

        layout.addWidget(label)
        self.setLayout(layout)