from PySide6.QtWidgets import QWidget, QLabel, QVBoxLayout
from PySide6.QtCore import Qt


class SettingsPage(QWidget):
    def __init__(self):
        super().__init__()

        layout = QVBoxLayout()

        label = QLabel(
            "PB7 Settings\n\n"
            "⚙ Configuration Panel"
        )

        label.setAlignment(Qt.AlignCenter)

        layout.addWidget(label)
        self.setLayout(layout)