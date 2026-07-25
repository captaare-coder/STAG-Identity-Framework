from PySide6.QtWidgets import QWidget, QLabel, QVBoxLayout
from PySide6.QtCore import Qt


class DashboardPage(QWidget):
    def __init__(self):
        super().__init__()

        layout = QVBoxLayout()

        label = QLabel(
            "PB7 Intelligence Studio\n\n"
            "Dashboard Online\n\n"
            "🟢 Core Systems Ready\n"
            "🟢 GUI Connected\n"
            "🟢 Modules Standing By"
        )

        label.setAlignment(Qt.AlignCenter)

        layout.addWidget(label)
        self.setLayout(layout)